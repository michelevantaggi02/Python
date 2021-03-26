import speech_recognition as sr
import subprocess
import json
import os
import time
ambienti = dict()
def carica_json():
    global ambienti
    f = open("ambienti.json","r")
    ambienti  = json.loads(f.read()) 
    print(ambienti)
    f.close()
carica_json()
recognizer_instance = sr.Recognizer()  # Crea una istanza del recognizer
run = True
lista_programmi = {}
aperto = 0
while run:
    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)
        print("Sono in ascolto... parla pure!")
        audio = recognizer_instance.listen(source)
        print("Ok! sto ora elaborando il messaggio!")
    try:
        text = recognizer_instance.recognize_google(audio, language="it-IT")
        text = text.lower().replace("zero", "0").replace("uno", "1")
        print("Google ha capito: \n", text)
        if "chiudi" in text:
            run = False
        elif "apri" in text:
            testo = text.split(" ")
            programma = ambienti[testo[1]]
            stringa = programma["posizione"]
            
            if programma["tipo"] == "ide":
                stringa += " "+programma["posizione progetti"]
            elif programma["tipo"] == "browser":
                if "profilo" in testo:
                    print(programma["lista profili"])
                    stringa+= " "+programma["scelta profilo"]+programma["lista profili"][int(testo[testo.index("profilo")+1])]
                else:
                    stringa+=" "+programma['scelta profilo']+"Default\""
                if "pagina" in testo:# or "scheda" in testo or "finestra" in testo:
                    stringa += " "+programma['nuova finestra']+" "+testo[testo.index("pagina")+1]
            elif programma["tipo"] == "link":
                stringa += programma[testo[-1]]
            else:
                print("MA PORCODDIO")
                raise Exception("non esiste nessun programma chiamato come questo") 
            print(stringa)
            aperto = subprocess.Popen(stringa, shell = False)
            print("PID: ",aperto)
    except Exception as e:
        print("errore ", e)
