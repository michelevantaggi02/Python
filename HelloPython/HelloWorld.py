lista = [10, 20 ,11, "f"] # modificabile generalmente si usa per oggetti uguali ma vanno bene anche diversi
tupla = ('abc', 123, 198.3) # non modificabile
dizionario = {"chiave":"valore", "numero":10, "oggetto":lista} 
# le chiavi possono essere solo di tipi "Hashtabili" 
#cioè se hanno un valore hash e possono essere comparati con altri oggetti
tipo = type(tupla)
a = "l'oggetto {} è un {} contiene {} oggetti"
f = a.format(tupla,tipo,len(tupla))
print(f)
#print("elemento minore",min(tupla),"elemento maggiore",max(tupla))
lista2 = [10, 11, 12, 10, 13]
conta = lista2.count(10)
minimo = min(lista2)
massimo = max(lista2)
print(conta, minimo, massimo)
lista2.sort()# riordina
print(lista2)

tabella = [("nome", "cognome", "eta"),
            ("Michele", "Vantaggi", 17)]
print(tabella)