import requests
from bs4 import BeautifulSoup

url = "https://temp-mail.org/en/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }

response = requests.get(url, headers=headers)

pagina = BeautifulSoup(response.content, "html.parser")

mail = pagina.find(id="mail").get("value")

print(mail)