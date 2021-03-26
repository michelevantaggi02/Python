from comandi import PC, funzioni, comandi
from time import sleep
f = open("emu\\Super Mario Bros. (World).nes", "rb")
tot = f.read()
print(tot[0:4])
check = tot[0:4]
if check == b'NES\x1a':
    print("FILE NES RICONOSCIUTO")
    print("NES 2.0",tot[7]&0x0C==0x08)
    mirroringV = False
    if tot[6] == 1:
        mirroringV = True
    if tot[7] != 0:
        print(tot[7])
    if tot[8] != 0:
        print(tot[8])
    header = tot[0:16]
    print(header)
    gioco = tot[16:]
    print(gioco[0:20])
    while True:
        #print(gioco[PC:PC+1])
        if comandi[gioco[PC:PC+1]][-1] == "#":
            print("     VAL",gioco[PC+1:PC+2],"->", int.from_bytes(gioco[PC+1:PC+2], "big", signed=False))
            funzioni[comandi[gioco[PC:PC+1]]](int.from_bytes(gioco[PC+1:PC+2], "big", signed=False))
            PC+=2
        elif comandi[gioco[PC:PC+1]][-1] == "$":
            val = bytes.hex(gioco[PC+2:PC+3]+gioco[PC+1:PC+2])
            print("     VAL",gioco[PC+1:PC+3],"->",val)
            funzioni[comandi[gioco[PC:PC+1]]](val)
            PC+=3
        else:
            funzioni[comandi[gioco[PC:PC+1]]]()
            PC+=1
        #sleep(1)
else:
    print("FILE NON VALIDO")