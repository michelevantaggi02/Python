import tkinter as tk
import classeviva as cv
from threading import Thread

def aggiorna_voti():
    print("Aggiorno i voti")
    global mostra_voti, bot, info
    info["text"] = "Aggiorno lista dei voti"
    voti["state"] = tk.DISABLED
    mostra_voti["state"] = tk.DISABLED
    bot.carica_voti()
    info["text"] = "Lista dei voti aggiornata"
    mostra_voti["state"] = tk.NORMAL
    voti["state"] = tk.NORMAL
def aggiorna_compiti():
    print("aggiorno i compiti")
    global mostra_compiti, bot, info
    info["text"] = "Aggiorno la lista dei compiti"
    compiti["state"] = tk.DISABLED
    mostra_compiti["state"] = tk.DISABLED
    bot.agenda()
    compiti["state"] = tk.NORMAL
    mostra_compiti["state"] = tk.NORMAL
    info["text"] = "Lista dei compiti aggiornata"
def connetti_registro():
    global bot, compiti, voti, connetti
    info["text"]= "Connessione al registro"
    bot.start()
    info["text"]= "Connesso"
    voti["state"]=tk.NORMAL
    compiti["state"]=tk.NORMAL
    connetti["state"]=tk.DISABLED
def chiudi():
    global interfaccia
    bot.stop()
    interfaccia.destroy()
bot = cv.bot()
interfaccia = tk.Tk()
voti = tk.Button(interfaccia,text="Aggiorna voti", state=tk.DISABLED, command=lambda : Thread(target=aggiorna_voti).start())
mostra_voti = tk.Button(interfaccia,text="Mostra i voti", state=tk.DISABLED, command=bot.mostra_voti)
compiti = tk.Button(interfaccia, text="Aggiorna i compiti", state=tk.DISABLED, command=lambda : Thread(target=aggiorna_compiti).start())
mostra_compiti = tk.Button(interfaccia, text="Mostra i compiti", state = tk.DISABLED, command=bot.mostra_agenda)
padd = 5
voti.grid(row=1, column=0, padx=padd,pady=padd)
mostra_voti.grid(row=2,column=0, padx=padd,pady=padd)
compiti.grid(row=1, column=1, padx=padd,pady=padd)
mostra_compiti.grid(row=2, column=1, padx=padd,pady=padd)
info = tk.Label(interfaccia)
info.grid(row=3, column=0, columnspan=2)
connetti = tk.Button(interfaccia, text="Connetti al registro", command=lambda : Thread(target=connetti_registro).start())
connetti.grid(row=0,column=0,padx=padd,pady=padd,columnspan=2)

interfaccia.protocol("WM_DELETE_WINDOW", chiudi)
interfaccia.mainloop()
