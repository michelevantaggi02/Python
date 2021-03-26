from time import sleep
a=[]
x=True
while x==True: 
    insert = input("Inserisci un numero, per finire scrivi n. ")
    if insert=="n":
        x=False
    else:
        a.append(insert)
print("Lista:",a)

for i in range(len(a)-2):
    cont = i
    for j in range(len(a)-2,cont+1, -1):
        if a[j]>a[j-1]:
            a[j], a[j-1]  =a[j-1], a[j]
            print("Lista:",a)
            sleep(0.5)