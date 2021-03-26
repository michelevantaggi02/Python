from selenium import webdriver
from selenium.webdriver.common import keys
import time

class bot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.bot = webdriver.Chrome(chrome_options=chrome_options)

    def start(self):
        self.bot.get("https://www.reddit.com")
        time.sleep(3)
        nsfw = self.bot.find_element_by_css_selector("#SHORTCUT_FOCUSABLE_DIV > div:nth-child(4) > div > div > div:nth-child(1) > div > div > div._3-bzOoWOXVn2xJ3cljz9oC > a._1HunhFR-0b-AYs0WG9mU_P.i2sTp1duDdXdwoKi1l8ED")
        if nsfw is not None:
            nsfw.click()

reddit = bot()
reddit.start()