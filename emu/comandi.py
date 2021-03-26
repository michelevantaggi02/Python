ram = {}
print("Mapping RAM...")
for i in range(65536):
    ram[("000" + hex(i)[2:])[-4:]] = 0
print("RAM mapped")
registri = {"A":0, "X":0, "Y":0, "SP":0}
flag = {"C":0, "Z":0, "I":0, "D":0, "V":0, "N":0, "B":0}
PC = 0
def checkZ(n):
    if n == 0:
        flag["Z"] = 1
    else:
        flag["Z"] = 0
def checkN(n):
    strin = "{0:08b}".format(n)
    flag["N"] = int(strin[0])
def log(string):
    print("                                                                                                                        ", end="\r")
    print(string)
    #interfaccia()
def interfaccia():
    print(registri, end="\r")
def lda(n):
    log("Registro A {} -> {}".format(registri["A"], n))
    registri["A"] = n
    checkZ(n)
    checkN(n)
def sta_ram(n):
    if n in ram.keys():
        log("Posizione {}: {} -> {}".format(n, ram[n], registri["A"]))
    else:
        log("Creo posizione {} = {}".format(n, registri["A"]))
    ram[n] = registri["A"]
    
def bpl(n):
    global PC
    log("Salto se Flag N == 0")
    log("PC: {}".format(PC))
    if flag["N"] == 0:
        PC+=n
    log("PC2: {}".format(PC))
def cld():
    flag["D"] = 0
    log("Clear Flag D")
def ldx(n):
    checkN(n)
    checkZ(n)
    registri["X"], n = n, registri["X"]
    log("Registro X {} -> {}".format(n, registri["X"]))
    
def txs():
    registri["SP"] = registri["X"]
    log("Sposto X-> stack pointer")
def lda_ram(n):
    registri["A"]=ram[n]
    log("Registro A da pos {} {}->{}".format(n, registri["A"], ram[n]))
    checkN(ram[n])
    checkZ(ram[n])
def sei():
    log("Set flag I")
    flag["I"]=1
def ldy(n):
    checkN(n)
    checkZ(n)
    registri["Y"], n = n, registri["Y"]
    log("Registro Y {} -> {}".format(n, registri["Y"]))
comandi = {
    b"\xd8":"CLD",
    b"\xa9":"LDA #",
    b"\x10":"BPL #",
    b"\x8d":"STA $",
    b"\xa2":"LDX #",
    b'\x9a':"TXS",
    b'\xad':"LDA $",
    b'x':"SEI",
    b'\xa0':"LDY #" 
}
funzioni = {
    "LDA #": lambda n: lda(n),
    "CLD": lambda : cld(),
    "BPL #": lambda n: bpl(n),
    "STA $": lambda n: sta_ram(n),
    "LDX #": lambda n: ldx(n),
    "TXS": lambda : txs(),
    "LDA $": lambda n : lda_ram(n),
    "SEI": lambda: sei(),
    "LDY #": lambda n : ldy(n)
}