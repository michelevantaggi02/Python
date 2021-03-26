import json

f = open("prove/recipes.json", "r")
jfile = json.loads(f.read())
f.close()
for i in jfile["recipes"]:
    title = "----------------------------{}----------------------------".format(i["name"])
    print(title)
    for j in i["ingredients"]:
        if j["amount"] == "q.s.":
            print("I need some", j["name"])
        elif j["unit"] is None:
            print("I need:", j["amount"], j["name"])  
        else:
            print("I need:", j["amount"], j["unit"], "of", j["name"])
    print("-"*len(title))
    j = i["creation"]
    for k in j["preparation"]:
        print("I need to", k)
    print("-"*len(title))
    for k in j["cooking"]:
        print(k["action"],"for",k["duration"],k["unit"], end="")
        if k["after"] is not None:
            print(", then",k["after"])
        else:
            print("")
    print("-"*len(title))
    for k in j["seasoning"]:
        print(k)
    print("-"*len(title))
    print("Serve",j["serving"])