import libraries.items as items


class inventario:
    def __init__(self, oggetti=[]):
        self.oggetti = oggetti
        #for i in range(len(oggetti)):
            #self.items.append = items.items(oggetti[i])
    def aggiungi(self, oggetto, qnt=1):
        for i in range(qnt):
            self.oggetti.append(oggetto)
    
    def rimuovi(self, oggetto, qnt=1):
        for i in range(qnt):
            try:
                self.oggetti.remove(oggetto)
            except ValueError as identifier:
                if i != 0:
                    print("Rimossi",i,oggetto)
                else:
                    print("impossibile rimuovere",qnt,oggetto)
            
    #def mostra(self):
    #    for i in items:
