class Pessoa:
    def __init__ (self, nome, idade, altura, peso, genero):
        self.nome = nome
        self.idade = int(idade)
        self.altura = float(altura)
        self.peso = float(peso)
        self.genero = genero
        self.comendo = False
        self.andando = False
        self.falando = False
        self.dormindo = False

    def comer(self, alimento):
        if not self.dormindo and not self.falando:
            print(f"{self.nome} está comendo {alimento}")
            self.comendo = True
        else:
            print(f"{self.nome} não pode comer porque está dormindo ou falando")

    def andar(self, destino):
        if not self.dormindo:
            print(f"{self.nome} está andando até {destino}")
            self.andando = True
        else:
            print(f"{self.nome} não pode andar porque está dormindo")

    def dormir(self, ondeDorme):
        if not self.andando and not self.falando and not self.comendo:
            print(f"{self.nome} está dormindo em {ondeDorme}")
            self.dormindo = True
        else:
            print(f"{self.nome} não pode dormir porque está falando ou andando")

    def falar(self, fala):
        if not self.dormindo and not self.comendo:
            print(f"{self.nome} está falando '{fala}'")
            self.falando = True
        else:
            print(f"{self.nome} não pode falar porque está dormindo ou comendo")

    def pararAndar(self):
        if self.andando:
            self.andando = False
            print(f"{self.nome} parou de andar")
        else:
            print(f"{self.nome} não está andando")

    def pararDormir(self):
        if self.dormindo:
            print(f"{self.nome} acordou")
            self.dormindo = False
        else:
            print(f"{self.nome} já está acordado")

    def pararComer(self):
        if self.comendo:
            print(f"{self.nome} parou de comer")
            self.comendo = False
        else:
            print(f"{self.nome} não está comendo")

    def pararFalar(self):
        if self.falando:
            print(f"{self.nome} parou de falar")
            self.falando = False
        else:
            print(f"{self.nome} não está falando")

pessoa1= Pessoa(nome= "Jubileu", idade= 37, altura= 1.98, peso = 102, genero = "Masculino")
pessoa1.andar("casa")     
pessoa1.dormir("cama")    
pessoa1.comer("bolo")     
pessoa1.pararComer()      
pessoa1.falar("Olá")      
pessoa1.pararFalar()      
pessoa1.pararDormir()    
pessoa1.pararAndar() 

