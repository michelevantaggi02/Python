import libraries.inventario as inventario
class Player:
    def __init__(self,nome, livello, exp,inv):
        self.nome = nome
        self.livello = livello
        self.exp = exp
        self.listaxp=[]
        for i in range(50):
            self.listaxp.append(i*100)
        self.inventario = inventario.inventario(inv)
    
    def aumentalv(self,n_livelli=1):
        self.livello = self.livello+n_livelli

    def aumentaxp(self, n_exp=10):
        self.exp = self.exp+n_exp
        if self.listaxp[self.livello]==self.exp:
            self.aumentalv()