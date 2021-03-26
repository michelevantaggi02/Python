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
        bot.get("https://www.amazon.it/Sony-PlayStation-5/dp/B08KKJ37F7/")
        toast = ToastNotifier()
        toast.show_toast("CONTROLLO AMAZON", "Avviato", duration=2, threaded=True)
        start = datetime.now()
        start = start.strftime("%H:%M:%S")
        while True:
            try:
                valore = bot.find_element_by_css_selector("#availability > span")
                testo = valore.get_attribute("innerText")
                if "Non disponibile." not in testo:
                    toast.show_toast("CONTROLLO AMAZON", testo, duration=100, threaded=True)
                    break
                adesso = datetime.now()
                adesso = adesso.strftime("%H:%M:%S")
                print(start + " -> "+adesso+" : "+testo, end="\r")
            except:
                print("\nErrore sito")
            bot.refresh()
            time.sleep(random()+1)
        
        bot.close()
        playsound(r"C:/Users/michi/Desktop/Informatica/Python/Selenium/amazon/Alarm.mp3")

amazon = bot()
amazon.start()