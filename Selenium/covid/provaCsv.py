import csv
import requests
import json

tab = requests.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv")
fopen = open("dati.csv", "wb")
fopen.write(tab.content)
fopen.close()
fopen = open("dati.csv", "r")
tabella = csv.reader(fopen, delimiter=",")
print(type(tabella))
lista = list(tabella)
print(lista[0])
for i in lista:
    print(i)