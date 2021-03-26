import requests
import json
import matplotlib.pyplot as pl

richiesta = requests.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json")

oggetto = json.loads(richiesta.text)
lista_nuovi = list()
lista_date = list()
lista_totale = list()
lista_ricoverati = list()
lista_deceduti = list()
lista_rateo = list()
data_prev = ""
prev_tamponi = 0
for i in oggetto:
    if data_prev != i["data"]:
        lista_nuovi.append(i["nuovi_positivi"])
        lista_totale.append(i["totale_positivi"])
        lista_ricoverati.append(i["totale_ospedalizzati"])
        lista_deceduti.append(i["deceduti"])
        lista_rateo.append(i["nuovi_positivi"]*100/(i["tamponi"]-prev_tamponi))
        prev_tamponi = i["tamponi"]
        data_prev = i["data"]
        lista_date.append(data_prev)
pl.plot(range(1, len(lista_date)+1), lista_nuovi, label="nuovi")
pl.plot(range(1, len(lista_date)+1), lista_totale, label="positivi")
pl.plot(range(1, len(lista_date)+1), lista_ricoverati, label="ricoverati")
pl.plot(range(1, len(lista_date)+1), lista_deceduti, label="deceduti")
legenda = pl.legend(frameon = False,bbox_to_anchor=(1, 1), loc= "upper left")
mng = pl.get_current_fig_manager()
mng.window.state("zoomed")
pl.show()
pl.plot(range(1, len(lista_date)+1), lista_rateo, label="% tamponi")
pl.show()