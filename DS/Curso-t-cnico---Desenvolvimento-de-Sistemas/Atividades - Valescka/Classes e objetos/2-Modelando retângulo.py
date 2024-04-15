# Crie uma classe que modele um retangulo:
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
#Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
class Retangulo:
  def __init__(self, ladoA, ladoB):
    self.ladoA = ladoA
    self.ladoB = ladoB
  def mudar_valor(self):
    self.ladoA = int(input("Digite o lado A: "))
    self.ladoB = int(input("Digite o lado B: "))
  def retornar_valor(self):
    print("Lado A: ", self.ladoA)
    print("Lado B: ", self.ladoB)
  def calcular_area(self):
    area = self.ladoA * self.ladoB
    print("Área: ", area)
  def calcular_perimetro(self):
    perimetro = (self.ladoA * 2) + (self.ladoB * 2)
    print("Perímetro: ", perimetro)
retangulo1 = Retangulo(0, 0)
retangulo1.mudar_valor()
retangulo1.retornar_valor()
retangulo1.calcular_area()
retangulo1.calcular_perimetro()