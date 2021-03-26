from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options
import time
from random import random
from win10toast import ToastNotifier
from playsound import playsound
from datetime import datetime

class bot:
    def __init__(self):
        opzioni = Options()
        opzioni.headless = True
        opzioni.add_argument("log-level=3")
        self.bot = webdriver.Chrome(executable_path="chromedriver.exe", options=opzioni)
    
    def start(self):
        bot = self.bot
        bot.get("https://www.eprice.it/playstation-5-SONY/d-13981612")
        toast = ToastNotifier()
        toast.show_toast("CONTROLLO EPRICE", "Avviato", duration=2, threaded=True)
        start = datetime.now()
        start = start.strftime("%H:%M:%S")
        while True:
            try:
                valore = bot.find_element_by_css_selector("#reactSpike > div > div > div > strong")
                testo = valore.get_attribute("innerText")
                if "ESAURITO O FUORI PROD." not in testo:
                    toast.show_toast("CONTROLLO EPRICE", testo, duration=100, threaded=True)
                    break
                adesso = datetime.now()
                adesso = adesso.strftime("%H:%M:%S")
                print(start + " -> "+adesso+" : "+testo, end="\r")
            except Exception as e:
                print("\nErrore sito: ", e)
            bot.delete_all_cookies()
            bot.refresh()
            time.sleep(random()*4+2)
        
        bot.close()
        playsound(r"C:/Users/michi/Desktop/Informatica/Python/Selenium/amazon/Alarm.mp3")

amazon = bot()
amazon.start()