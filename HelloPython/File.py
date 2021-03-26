try:
    oggetto = open("ciao.txt", "w")
except FileNotFoundError as identifier:
    print(identifier)
else:
    oggetto.write("Ciao Mondo!\n")
    oggetto.write("Hello World!\n")
    oggetto.write("Porco il Mondo")
    oggetto.close()
    oggetto = open("ciao.txt")
    #print(leggi)
    leggi = oggetto.readlines()
    for i in leggi:
        if i.lower().__contains__("mondo") :
            print("Mondo Ciao")
        else:
            print("Boh")
oggetto.close()