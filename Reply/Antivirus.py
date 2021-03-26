inp = open("input-antivirus-763c.txt","r")
TCN = inp.readline()
for i in range(int(TCN)):
    wordletters = inp.readline().split(" ")
    virlen = int(inp.readline())
    frasi = []
    first = inp.readline()
    risposta = ""
    
    
    for x in range(len(wordletters)-1):
        
        frasi.append(inp.readline())
    print(frasi)
        
    for y in range(len(wordletters[0])-(virlen-1)):
        maybe = first[i:i+(virlen)]
        print(maybe)
        
        for j in range(len(frasi)):
            

            sampled = frasi[j]
            
                
            for x in range(len(sampled)-(virlen-1)):
                if sampled[x:virlen] == maybe:
                    risposta= risposta+str(x)+" "
    print(risposta)
                    
                    
                    
            
        
    
