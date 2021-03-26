import fractions
lista = [10, 20 ,11]
lista.append(13) #aggiunge un elemento alla lista
provaSet = {12, 12, 23 , 41}#set
provaFrozenSet = {10, 122, 45}#frozenset
#set e frozenset sono simili alle liste e ai tuple solo che vanno inseriti valori unici
#nei set e nei frozenset devi inserire tipi "Hashtabili"
#set ha elementi in comune con gli insiemi vedi:https://www.html.it/pag/65165/set-e-frozenset/
dizionario = {"chiave":"valore", "numero":10, "oggetto":provaSet} 
dizionario.__setitem__("prova",11)
# le chiavi possono essere solo di tipi "Hashtabili" 
#cioè se hanno un valore hash e possono essere comparati con altri oggetti
del dizionario["chiave"] #elimina sia la chiave che il valore
chiave = dizionario["numero"]
default = dizionario.get("prova", "errore") #se si inserisce una chiave non esistente restituisce il valore di default
print("Valore:",chiave)
print("Dizionario:",dizionario)
print("Default:",default)