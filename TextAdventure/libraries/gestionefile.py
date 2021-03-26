def salvataggio(nome,livello,exp):
    nome = nome+"\n"
    livello = str(livello)+"\n"
    exp = str(exp)+"\n"
    salvataggio = open("salvataggi/salvataggio.save", "w")
    salvataggio.write(nome)
    salvataggio.write(str(livello))
    salvataggio.write(str(exp))