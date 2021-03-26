import matplotlib.pyplot as mp
import time
prova = ["cristoaaaaaaaaaaaaaaaaaaaa", "maria", "io", "no"]
valore = [[10, 20, 30, 40],[40,20,10,5],[35,11,55,22],[42,31,20,9]]
aaa = [0, 1, 2, 3]
mp.tight_layout()
for i in range(len(prova)):
        mp.plot(aaa, valore[i], )
        mp.yticks(valore[i], prova)
mp.show()

