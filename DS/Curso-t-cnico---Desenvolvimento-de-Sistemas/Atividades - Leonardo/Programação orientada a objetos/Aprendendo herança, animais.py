class Animal:
    def __init__(self, nome, idade, cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.andando = False
        self.dormindo = False
        self.comendo = False
        self.fazendoSom = False

    def fazerSom(self, som):
        if not self.dormindo and not self.comendo:
            self.fazendoSom = True
            print(f"{self.nome} está emitindo som: {som}")
        else:
            print(f"{self.nome} não pode emitir som porque está dormindo ou comendo.")

    def andar(self, destino):
        if not self.dormindo:
            self.andando = True
            print(f"{self.nome} está andando até {destino}.")
        else:
            print(f"{self.nome} não pode andar porque está dormindo.")

    def dormir(self, onde):
        if not self.andando and not self.fazendoSom and not self.comendo:
            self.dormindo = True
            print(f"{self.nome} está dormindo em {onde}.")
        else:
            print(f"{self.nome} não pode dormir porque está andando, emitindo som ou comendo.")

    def comer(self, alimento):
        if not self.andando and not self.fazendoSom and not self.dormindo:
            self.comendo = True
            print(f"{self.nome} está comendo {alimento}.")
        else:
            print(f"{self.nome} não pode comer porque está andando, emitindo som ou dormindo.")

    def pararFazerSom(self):
        self.emitindo_som = False

    def pararAndar(self):
        self.andando = False

    def pararDormir(self):
        self.dormindo = False

    def pararComer(self):
        self.comendo = False

class Cachorro(Animal):
    def __init__(self, nome, idade, raca, cor):
        super().__init__(nome, idade, cor)
        self.raca = raca

    def emitir_som(self, som="Au Au!"):
        super().FazerSom(som)

animal1 = Cachorro(nome="Arthur", idade=3, cor= "marrom", raca = "husky")
animal1.andar("parque")
animal1.dormir("casa")
animal1.comer("racao")
animal1.fazerSom("Au Au")