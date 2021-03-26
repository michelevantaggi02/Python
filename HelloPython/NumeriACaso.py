from random import randint
numero = randint(0, 100)
mosse = 0
while True:
    mosse+=1
    try:
        inserito = input("Inserisci un numero: ")
        numeroInserito = int(inserito)
    except ValueError:
        print(inserito,"non è un numero")
    else:
        if numero == numeroInserito:
            print("Complimenti, hai vinto in",mosse,"mosse!")
            break
        elif numeroInserito > numero:
            print("Il numero estratto è più piccolo")
        elif numeroInserito < numero:
            print("Il numero estratto è più grande")