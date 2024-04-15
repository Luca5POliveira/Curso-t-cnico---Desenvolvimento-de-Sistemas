#Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
class Quadrado:
     def __init__(self, lado):
         self.lado = lado

     def mudar_lado(self, novo_lado):
         self.lado = novo_lado

     def retornar_lado(self):
         return self.lado

     def calcular_area(self):
         return self.lado ** 2
meu_quadrado = Quadrado(5)
print("Lado do quadrado:", meu_quadrado.retornar_lado())
meu_quadrado.mudar_lado(7)
print("Novo lado do quadrado:", meu_quadrado.retornar_lado())
print("A área do quadrado é: ", meu_quadrado.calcular_area())
