# Crie uma classe que modele uma pessoa:
#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: 
#Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            self.altura += 0.5 * anos
    def engordar(self, peso):
        self.peso += peso
    def emagrecer(self, peso):
        self.peso -= peso
    def crescer(self, altura):
        self.altura += altura
pessoa1 = Pessoa(nome="João", idade=20, peso=70, altura=170)
print("Antes:")
print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade)
print("Peso:", pessoa1.peso)
print("Altura:", pessoa1.altura)
pessoa1.envelhecer()
pessoa1.engordar(5)
pessoa1.emagrecer(3)
pessoa1.crescer(2)
print("\nDepois:")
print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade)
print("Peso:", pessoa1.peso)
print("Altura:", pessoa1.altura)