files = open("input-party-0f71.txt")
leggi = files.readlines()
times = int(leggi[0])
final = list()
counter = 0
for i in range(0,times*2,2):
    friends = int(leggi[i+1])
    amicizia = leggi[i+2].split()
    sum=0
    for j in amicizia:
        j = int(j)
        if j>0:
            sum+=j
    counter+=1
    final.append("Case #"+str(counter)+": "+str(sum)+"\n")
    print("Case #",counter,": ",sum,sep="")
output = open("output.txt","w+")
output.writelines(final)