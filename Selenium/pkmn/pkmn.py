import requests
import json
import matplotlib.pyplot as plt

f = requests.get("https://www.pokemon.com/it/api/pokedex")
obj = json.loads(f.text)
tipi = {}
deb = {}
altezza = 0
for i in obj:
    for j in i["type"]:
        if(j in tipi.keys()):
            tipi[j] += 1
        else:
            tipi[j] = 1
    for j in i["weakness"]:
        if(j in deb.keys()):
            deb[j] += 1
        else:
            deb[j] = 1
    altezza += i["height"]
figure, (a1, a2) = plt.subplots(1, 2)
print(altezza/len(obj))
a1.pie(tipi.values(), labels= tipi.keys(), autopct='%1.1f%%',  labeldistance=1.03)
a1.set_title("Tipi")
a2.pie(deb.values(), labels= deb.keys(), autopct='%1.1f%%',  labeldistance=1.03)
a2.set_title("Debolezze")
plt.subplots_adjust(left=0.02, top=1, bottom=0, right=0.96)
mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt.show()