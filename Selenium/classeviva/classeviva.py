from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as mp
import keyboard
import time

class bot:
    def __init__(self):
        opzioni = Options()
        opzioni.headless = True
        opzioni.add_argument("log-level=3")
        self.bot = webdriver.Chrome(executable_path="chromedriver.exe", options=opzioni)
        self.conta = []
        self.prof= []
        self.colori = []
        self.materie = []
        self.voti = []
        
        self.fig, self.ax = mp.subplots()

    def start(self):
        """Si connette al registro elettronico ed effettua l'accesso"""
        self.bot.get("https://web.spaggiari.eu/home/app/default/login.php")
        time.sleep(1)
        account = self.bot.find_element_by_css_selector("#login")
        account.send_keys("S5662414I")
        password = self.bot.find_element_by_css_selector("#password")
        password.send_keys("vm36495y") #evitamo de farla vede grazie
        invia = self.bot.find_element_by_css_selector(".check-auth")
        invia.click()
        time.sleep(3)
    
    def stop(self):
        """Chiude il bot"""
        self.bot.close()

    def onpick(self,e):
    # on the pick event, find the orig line corresponding to the
    # legend proxy line, and toggle the visibility
        legline = e.artist
        origline = self.dizionario[legline]
        print(origline)
        vis = not origline.get_visible()
        origline.set_visible(vis)
        
    # Change the alpha on the line in the legend so we can see what lines
    # have been toggled
        if vis:
            legline.set_alpha(1.0)
        else:
            legline.set_alpha(0.2)
        self.fig.canvas.draw()

    def agenda(self):
        """Apre l'agenda su cui sono scritti compiti e comunicaioni"""
        self.bot.get("https://web.spaggiari.eu/fml/app/default/agenda_studenti.php")
        time.sleep(3)
        compiti = self.bot.find_elements_by_css_selector("#full > div > div > div > div > div > span.fc-event-title > font")
        print("totale compiti: "+str(len(compiti)))
        
        #conta i compiti e i vari prof
        for i in compiti:
            prof = self.prof
            conta = self.conta
            colori = self.colori
            testo = i.text.replace(":", "").replace("COMPITI DI ", "").replace(" ", "\n")
            if i.text not in prof:
                prof.append(testo)
                conta.append(0)
                colori.append("cyan")
            pos = prof.index(testo)
            conta[pos]+=1
            
        massimo = max(conta)
        massimo2 = 0
        for i in range(len(conta)):
            if conta[i] == massimo:
                colori[i]="r"
            elif conta[massimo2] < conta[i]:
                massimo2 = i
        colori[massimo2] = "orange"
        indietro = self.bot.find_element_by_css_selector("#data_table > tbody > tr:nth-child(6) > td:nth-child(7) > a")
        indietro.click()
        time.sleep(3)
        
    def mostra_agenda(self):
        """
        mostra un grafico relativo a quanti compiti sono stati dati dai vari professori.
        DA CHIAMARE DOPO agenda()
        """
        lista = mp.bar(self.prof, self.conta, color=self.colori)
        mp.suptitle("Annotazioni questo mese")
        mp.xlabel("Professori/Materie")
        mp.ylabel("N annotazioni")
        #mp.xticks(rotation=-90)
        mng = mp.get_current_fig_manager()
        mng.window.state("zoomed")
        mp.show()
    
    def carica_voti(self):
        """Conta i voti ricevuti nelle varie materie"""
        materie = self.materie
        self.bot.get("https://web.spaggiari.eu/cvv/app/default/genitori_note.php")
        time.sleep(3)
        mostra_tabella = self.bot.find_element_by_css_selector("#data_table > tbody > tr.griglia.noprint > td:nth-child(5) > a")
        mostra_tabella.click()
        time.sleep(1)
        righe = self.bot.find_elements_by_css_selector("#S1 > div.inner > table > tbody > tr.riga_materia_componente")
        for i in righe:
            materia = i.find_element_by_css_selector("div.materia_desc")
            materie.append(materia.text)
            lista_voti = i.find_elements_by_css_selector("p.s_reg_testo")
            voti = []
            for j in lista_voti:
                valore = j.text.replace("½", ".5").replace("+", ".25").replace("-", ".75")
                valore = float(valore)
                if j.text.__contains__("-"):
                    valore -=1
                voti.append(valore)
            #print("Voti di {}: {}".format(materia.text, voti))
            self.voti.append(voti)
        indietro = self.bot.find_element_by_css_selector("#data_table > tbody > tr.griglia.noprint > td:nth-child(2) > a")
        indietro.click()
        time.sleep(3)
    
    def mostra_voti(self):
        """Mostra un grafico relativo ai voti delle varie materie
        DA CHIAMARE DOPO carica_voti()"""
        materie = self.materie
        linee = []
        for i in range(len(materie)):
            linea = mp.plot(range(1, len(self.voti[i])+1), self.voti[i], label = materie[i], marker="o")
            print(linea)
            linee.append(linea)
        mp.subplots_adjust(left=0.036, right=0.81)
        legenda = mp.legend(frameon=False,bbox_to_anchor=(1, 1), loc='upper left')
        self.dizionario={}
        for l_legenda, l_originale in zip(legenda.get_lines(), linee):
            l_legenda.set_picker(5)
            self.dizionario[l_legenda] = l_originale[0]
        print(self.dizionario)
        mng = mp.get_current_fig_manager()
        self.fig.canvas.mpl_connect('pick_event', self.onpick)
        mng.window.state("zoomed")
        mp.show()
        

    



if __name__ == "__main__":
    c = bot()
    c.start()
    while True:
        comando = input("richiedi qualcosa:").lower()
        
        if comando == "voti":
            c.carica_voti()
            c.mostra_voti()
        elif comando in ["compiti", "agenda"]:
            c.agenda()
            c.mostra_agenda()
        elif comando in ["chiudi", "esci"]:
            c.stop()
            break
        else:
            print("comando non valido")    