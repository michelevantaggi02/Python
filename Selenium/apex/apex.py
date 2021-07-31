import requests
import matplotlib.pyplot as plt
import json

username = "michi_vanta"
plat = "origin"
f = requests.get("https://public-api.tracker.gg/v2/apex/standard/profile/{}/{}".format(plat, username), headers={"TRN-Api-Key" : "dd5ad49b-a12e-41ec-a9be-cdfe4e3ec87b"})
testo = f.text
print(testo)


fi = open("sav.json","w")
fi.write(testo)
fi.flush()
fi.close()
kill = {}

fil= json.loads(testo)
for i in fil["data"]["segments"]:
    if i["type"] == "legend" and "kills" in i["stats"].keys():
        kill[i["metadata"]["name"]] = i["stats"]["kills"]["value"]

plot = plt.bar(kill.keys(), kill.values())
plt.title(username)
plt.get_current_fig_manager()
plt.show()