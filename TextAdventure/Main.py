import libraries.gestionefile as gestionefile
import libraries.player as player
livello = 0
exp = 0
try:
    salvataggio = open("salvataggi/salvataggio.save")
    leggi = salvataggio.readlines()
    nome = leggi[0]
    livello = int(leggi[1])
    exp = int(leggi[2])
    for i in leggi:
        print(i)
except FileNotFoundError as identifier:
    print("Nessun salvataggio presente")
    nome = input("Inserisci il tuo nome: ")
    gestionefile.salvataggio(nome,livello,exp)

giocatore = player.Player(nome,livello,exp)

