import json
import random
from tensorflow.python.framework import ops
import tensorflow as tf
import tflearn
import numpy as np
import nltk
import pickle

from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


with open("intents.json") as file:
    dati = json.load(file)

try:
    with open("dati.pickle", "rb") as f:
        parole, etichette, train, out = pickle.load(f)
except:
    parole = []
    etichette = []
    docs_x = []
    docs_y = []

    for intent in dati["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            parole.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])
            if intent["tag"] not in etichette:
                etichette.append(intent["tag"])

    parole = [stemmer.stem(w.lower()) for w in parole if w != "?"]
    parole = sorted(list(set(parole)))

    etichette = sorted(etichette)

    train = []
    out = []

    out_vuoto = [0 for _ in range(len(etichette))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w) for w in doc]

        for w in parole:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        out_riga = out_vuoto[:]
        out_riga[etichette.index(docs_y[x])] = 1

        train.append(bag)
        out.append(out_riga)

    train = np.array(train)
    out = np.array(out)

    with open("dati.pickle", "wb") as f:
        pickle.dump((parole, etichette, train, out), f)

ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(train[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(out[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("modello.tflearn")
except:
    model.fit(train, out, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("modello.tflearn")

def bag_of_words(s, parole):
    bag = [0 for _ in range(len(parole))]

    s_parole = nltk.word_tokenize(s)
    s_parole = [stemmer.stem(parola.lower()) for parola in s_parole]

    for se in s_parole:
        for i, w in enumerate(parole):
            if w == se:
                bag[i] = 1
    return np.array(bag)

def chat():
    print("Parla con il bot! (Scrivi quit per fermarti)")
    while True:
        inp = input("Tu: ")
        if inp.lower() == "quit":
            break
        risultato = model.predict([bag_of_words(inp, parole)])
        indice = np.argmax(risultato)
        etichetta = etichette[indice]
        
        for tag in dati["intents"]:
            if tag["tag"] == etichetta:
                risposte = tag["responses"]
        print(random.choice(risposte))

chat()