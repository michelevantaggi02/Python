def funzione(*nome):
    print("Ciao {}".format(", ".join(nome)))

def funzione2(element, **attrs):
    attrs = ' '.join(['{}="{}"'.format(k, v) for k, v in attrs.items()])
    return '<{} {}>'.format(element, attrs)

funzione("michi","luigi","peppe")
#print(funzione2("p",id="prova"))

def dizionario(**attributi):
    """mostra una lista di tutti i valori con i loro nomi"""
    attributi= " ".join(['{}={}'.format(chiave, valore) for chiave, valore in attributi.items()])
    # serve anche a mostrare chiavi e valori del dizionario
    return attributi
print(dizionario(id="gatto",valore="peppe",numero=10))