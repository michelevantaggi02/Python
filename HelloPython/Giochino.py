from random import randint
from time import time
from math import floor
listaParole =   ("pannolino","tomassini","mutande","computer","sedia","keyblade","tartaruga","tavolo",
                "schifo","borderlands","fucile","zombie","puffo","cancro","quaterback","oro","topolino",
                "flavio","gay","stadio")
gioco=True
while gioco:
    tempo = time()
    parola = randint(0, len(listaParole)-1)
    print(listaParole[parola])
    scritta = input()
    diversa=True
    for i in scritta:
        if scritta[scritta.__len__()-1-i] != listaParole[parola][i] and diversa:
            diversa = False

    if not diversa:
        print("Hai sbagliato parola")
    else:
        print("Complimenti, hai vinto.")
    tempo2 = floor(time()-tempo)
    print("Hai impiegato",tempo2,"secondi")
    continua = input("Vuoi continuare?\n")
    if continua.lower() != "si":
        gioco=False