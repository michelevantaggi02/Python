import json
import requests
import matplotlib.pyplot as mp
import matplotlib as lib
mp.style.use('dark_background')
lista_colori=["#F037E0", "#DB5A27", "#7040FF", "#0843a8","#ab1327","#428005","#519684","#967b3f","#FC1258","#39375B","#6B7D04","#1098F7","#EF767A","#32a852","#BC5D2E","#CEE7E6","#878E99","#E6F14A","#C3D350"]
lib.rcParams["axes.prop_cycle"]=lib.cycler(color=lista_colori)

dictlinee = dict()
medie = dict()
traduzioni = dict()
fig = None
pos_file = "C:/Users/michi/Desktop/Workspace/Python/Selenium/COD/medie.json"
def onpick(event):
    global fig
    # on the pick event, find the orig line corresponding to the
    # legend proxy line, and toggle the visibility
    legline = event.artist
    origline = dictlinee[legline]
    vis = not origline.get_visible()
    origline.set_visible(vis)
    # Change the alpha on the line in the legend so we can see what lines
    # have been toggled
    if vis:
        legline.set_alpha(1.0)
    else:
        legline.set_alpha(0.2)
    fig.canvas.draw()

def carica_json():
    global medie, traduzioni,f,pos_file
    f = requests.session()
    payload = {
        "Host": "my.callofduty.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": '_scid=d25daf0e-2e0a-46a8-8291-fc24418b4415; _gcl_au=1.1.665292975.1610648060; aamoptsegs=aam%3D16648913%2Caam%3D16187168; OptanonAlertBoxClosed=2021-01-14T18:14:46.581Z; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D; _ga=GA1.2.272073123.1610648087; _fbp=fb.1.1610648087010.832424097; optimizelyEndUserId=oeu1610648089111r0.8041552830905836; _ga=GA1.3.272073123.1610648087; _gid=GA1.3.1356593527.1611748512; _abck=585C7FE114072097C52530ED16FA8C0D~0~YAAQPBRlX436xTx3AQAAy6uyQwVHM3GxmVItb9j63Y9TZvM/aowz0yc+HMXE3nsgLY1Q0JntuPfJCvarHZySx/rivfGs1ycy9sXNl/OsA9ra7WwJm08xptygds8MCD/E/CFD4Jp18shIRY7WI/WnIDZ7FqZDzDHE5V23wGHyYTt/50XGCl9O0H1fReBWppMlIJt6EeB5JFcC95I3bqjSwwgwMqib9GU7ijEq7vxzUzlNiMAjmgqEWUgb5pM0TCt8jAmFe7Mvm9UmJIhucxv0Nxa7qGSmGhDSMWQfspVwl8+2owtrdWI9tY/qZ3Zo6uHAI23Ma5+KH8qo9KwvBj/gKU8+VN+ms+52OyA=~-1~-1~-1; umbrellaId=16704638157170148895; CRM_BLOB=eyJ2ZXIiOjEsInBsYXQiOnt9fQ; tfa_enrollment_seen=true; ssoDevId=8d31691e9d5d47d0bfd6613565ad3e14; new_SiteId=cod; _gid=GA1.2.1289307174.1611766587; AMCVS_0FB367C2524450B90A490D4C%40AdobeOrg=1; s_cc=true; XSRF-TOKEN=51bVdkvGcFi06zLVqcnHjd6vU3oOboDvQNGrWFVcynLHibf1uEEt0kls1NHymkCP; comid=cod; bm_sz=89A3EF55EE041F30B8AF38EA0159B131~YAAQzA4VAgDlRz53AQAAHWbGRAo067ntN8AhWZqgpk0W+XHlL7apWIjLMK0o9XbAL3bCOzCwjUBgpWnm75HHmGUBKTViuLyKHu2tCsnCpn8uDraDCRZqnfHvuZ6ia9UomVpTYkAY9WNAW7cyBA1G50FmvVWhdGd7ReHPZy4SmgaHsV8jQmxjXEhC+6Y3Cy4+1imwlA==; ACT_SSO_LOCALE=en_US; agegate=""; country=IT; at_flavor=""; bm_mi=DBF495C2C7BA1DD4B5821B14F69D0EDD~zaIx63ZApWP19Mz7HVteW24BzjBD+//Dzu9LXuiqIPRurt7X8aWStMAHO/5q/WKZBR1SEQxaAsSw4wLtVM55EEZpyxnQV7EKyMUPL1UMoo6WAigwbNbVYqzTFSaeYwIKZDwoUHIxru5RKfiIHTw3gS/D05FhLdbqXF6v0N/paYONVtswj2er76yTQ76gWMlPuaO75Crw6smn1lrhTTiL7yRbAPLlPvsR7W+9x/fVS4UEPazF8DdRzNfPG3kCIbcbOivAJ2+gC1F60cboeZNWIQ==; ak_bmsc=CBF64ED8117246F08018D23561901FDDC316C8363D7F0000339B1160C4CDE657~pldx8wr2bigufZyBS3Av3mij90ccft9M2W/dhyG6iI/1GUBDBR58KBftXH+sWJho9Zy8HbZRyG3KRtMizKAbjLXqNwixBI9ss4GLsIJNpNDXn0HPYOOxKNP4kKgh4QATQOl/Vtr8XXW1HUmvT1jXn3AYm1bBt8I5lil8pqaPjBZhru1xNk4bGq7mwuAIT+oOcUxtOOMv3wHb3i2f1wFL6Km33j8YyCUYOOugnXSoJu/j6JQL1NLZAf4/ab4B6vKBzG; THIRD_PARTY_AUTH_STATE=1611766620348X884735712134404200; ACT_SSO_COOKIE=NTEwNjY4NTM4NzA4NjU5Njk3NDoxNjEyOTc2MjIyNTc2OjgyYmNmMmJkZDY0ZGVmMDYyMGM4OGI2OTFkMTg2MDdj; ACT_SSO_COOKIE_EXPIRY=1612976222576; atkn=eyJhbGciOiAiQTEyOEtXIiwgImVuYyI6ICJBMTI4R0NNIiwgImtpZCI6ICJ1bm9fcHJvZF9sYXNfMSJ9.N_WUIqK6tVlSwImZeoB6rZlpXNqwEWhKs5k8f_b8ngM6MSq7XUonog.75xnWNHhFfuvqhv3.4LeGSwSQT36cjpa2TH68aJlTuVIrDPVWqXHOJ9JX_tlKKccdOH0mKnQ78kxCDym6F0UmyVpDyCAt2RsXCo1usD5koHBysbAfLxTshZJzXL3jvYaq1WNBpiYYt3pt5e5NzS9TrQY-X38-S56eWDaWvYYRk7zCFTg6CDRTuI-8ZJX_PPbYs2rEfPd2ldmq7deYVXewaYhz9lSzH9dtpvpU-C8E4uvA7Axjoj5cwbpjdQ6PUYDb-qeGaBqPK8EQbLAOCkTdsGBmTLITjaH1ZYABaAAw8kE1uK-QlNqNeIY9RCd6gc2NqeKTWV8D6BBISIuk-Xls2BfyE8i1yrXTPinjnlzkp-K5_loLQeVEPW2MzvNnE1j7gb8WPGeSFj7INW7Jtw9BKgNPvu3NL3wFlDvm_HW1OVoQX5TIF3zZ5qA7JVPdUcPlywiG2AB_b7TH9gyKlmWeptPPwqkBRwPcA5bol4O2j_8.W-E2AZy2hNYHfkKDN94upQ; sso_invalidate_cache=true; ACT_SSO_EVENT="LOGIN_SUCCESS:1611766622579"; pgacct=battle; AMCV_0FB367C2524450B90A490D4C%40AdobeOrg=-637568504%7CMCIDTS%7C18655%7CMCMID%7C65675560116072390702944951128455214719%7CMCAAMLH-1612371424%7C6%7CMCAAMB-1612371424%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1611773824s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C209050765; gpv_pn=callofduty%3Amycod%3Aplayer%3Arecentmatches; s_sq=%5B%5BB%5D%5D; s_nr=1611766725832-Repeat; s_tp=1312; s_ppv=callofduty%253Amycod%253Aplayer%253Arecentmatches%2C71%2C71%2C937; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jan+27+2021+17%3A58%3A46+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=6.10.0&hosts=&consentId=cd5ccd53-3d32-4ec7-af47-cb07f06450ae&interactionCount=2&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&AwaitingReconsent=false&geolocation=IT%3B55; bm_sv=421E6CE05C6D33090B9D037EB29AA125~A5mPfgpgzUUccHwjzurFOGVy3jE67/eiSPQLCyKPpkMDuZ5dZPImgAREi4V+n8VfnvaXiuDRTpF1xL1TrPTyJi2RmDpePrYDcihwcXpwYKBj3tLlNowyeJX5k8FWdV5hdF52WC9FZAANqx6TJlQnid+aDT3113nCkssmG5pNjhs='
    }
    f = requests.get(
        "https://my.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/battle/gamer/michivanta%232564/matches/mp/start/0/end/0/details", headers=payload)

    f = f.text
    f = json.loads(f)
    traduzioni = requests.get("https://my.callofduty.com/content/atvi/callofduty/mycod/web/it/data/json/iq-content-xweb.js")
    traduzioni = json.loads(traduzioni.text)
    
    file_medie = open(pos_file, "r")
    stringa_medie = file_medie.read()
    medie = json.loads(stringa_medie)
    file_medie.close()
    last = 0
    if "lastGamePlayed" in list(medie.keys()):
        last = medie["lastGamePlayed"]
    else:
        medie["lastGamePlayed"] = list()
    if "generale" not in list(medie.keys()):
        medie["generale"] = list()
    print("ULTIMA PARTITA SALVATA: ", last)
    
    medie["lastGamePlayed"] = f["data"]["matches"][0]["utcEndSeconds"]
    print("ULTIMA PARTITA GIOCATA: ", medie["lastGamePlayed"])
    nuove = dict()
    for i in list(medie.keys())[1:]:
        nuove[i] = []
    for i in f["data"]["matches"]:
        if i["utcEndSeconds"] > last:
            if i["playerStats"]["deaths"] == 0:
                i["playerStats"]["deaths"] = 1
            media = i["playerStats"]["kills"]/i["playerStats"]["deaths"]
            if i["map"] in medie.keys() :
                nuove[i["map"]].append(media)
            else:
                medie[i["map"]] = []
                nuove[i["map"]] = [media]
            nuove["generale"].append(media)
        else:
            break
        #print(i["map"])
    for i in list(medie.keys())[1:]:
        print(i)
        nuove[i].reverse()
        medie[i] = medie[i]+ nuove[i]
    print(list(medie.keys()))
    scrivi_medie = open(pos_file, "w")
    stringa_medie = json.dumps(medie)
    scrivi_medie.write(stringa_medie)
    scrivi_medie.close()

    

def mostra_grafico():
    global medie,traduzioni, fig
    fig, ax = mp.subplots()
    linee = []
    tot_partite = 0

    #medie["generale"].reverse()
    linea = mp.plot(range(1, len(medie["generale"])+1), medie["generale"], label ="generale", marker="o")
    linee.append(linea[0])

    for i in list(medie.keys())[2:]:
        #medie[i].reverse()
        tot_partite += len(medie[i])
        linea = mp.plot(range(1, len(medie[i])+1), medie[i], label = traduzioni["maps:mw-{}:1".format(i)], marker="o")
        linee.append(linea[0])
    
    legenda = mp.legend(frameon = False,bbox_to_anchor=(1, 1), loc= "upper left")

    for l_legenda, l_originale in zip(legenda.get_lines(), linee):
            l_legenda.set_picker(5)
            dictlinee[l_legenda] = l_originale
            
    mng = mp.get_current_fig_manager()
    mng.window.state("zoomed")
    mp.subplots_adjust(left=0.02, top=0.967, bottom=0.03, right= 0.895)
    fig.canvas.mpl_connect('pick_event', onpick)
    fig.canvas.set_window_title("Stats call of duty")
    mp.title("Partite salvate: {}".format(tot_partite))
    mp.show()

def stats():
    global f, traduzioni,lista_colori
    
    modalita = []
    tradotte = []
    sommario = f["data"]["summary"]
    richieste = ["kdRatio", "scorePerGame","scorePerMinute", "longestStreak","wlRatio", "rank"]
    
    for i in sommario:
        modalita.append(i)

    tradotte.append("generale")
    for i in modalita[1:]:
            tradotte.append(traduzioni["game-modes:mw-{}:1".format(i)])

    
    len_x = int(len(richieste)/2)
    len_y = int(len(richieste)/len_x)
    figure, assi = mp.subplots(len_x, len_y, sharex="col")

    for r in range(len(richieste)):
        valori = []
        for i in sommario:
            valori.append(sommario[i][richieste[r]])
        
        x = int(r/2)
        y= int(r%len_y)   
        assi[x,y].bar(tradotte, valori, color = lista_colori)
        assi[x,y].set_title(richieste[r])
        mp.setp(assi[x,y].get_xticklabels(), rotation=30)
        #mp.bar(tradotte, valori)
    mp.subplots_adjust(left=0.02, top=0.96, bottom=0.105, right=0.99, wspace= 0.057, hspace=0.117)
    mng = mp.get_current_fig_manager()
    mng.window.state("zoomed")
    mp.show()
def pie():
    global medie, traduzioni
    fig, ax = mp.subplots()
    valori = []
    tradotto = []
    for i in list(medie.keys())[2:]:
        valori.append(len(medie[i]))
        tradotto.append(traduzioni["maps:mw-{}:1".format(i)])
    
    #print(len(valori), len(traduzioni[:len(valori)-2]))
    lib.rcParams["font.size"] = 8
    mp.pie(valori, labels=tradotto,  autopct='%1.1f%%', pctdistance=1.05, labeldistance=1.2, shadow=True)
    mng = mp.get_current_fig_manager()
    mng.window.state("zoomed")
    mp.subplots_adjust(left=0, top=1, bottom=0, right= 1)
    mp.title("Torta partite")
    mp.show()
carica_json()
#mostra_grafico()
#stats()
pie()