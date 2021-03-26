dati = open("")
valori = dati.readlines()
times = int(valori[0])
for i in range(0,times*2,2):
    tests = valori[i+1]
    passaggi = valori[i+2].split()
    for j in range(len(passaggi)):
        passaggi[j]=int(passaggi[j])
        