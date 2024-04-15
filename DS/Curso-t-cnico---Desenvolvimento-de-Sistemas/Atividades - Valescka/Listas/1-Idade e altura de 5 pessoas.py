#1 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
#Imprima a idade e a altura na ordem inversa a ordem lida.
idades = []
alturas = []
for i in range(5):
  idade = int(input("Digite sua idade: "))
  altura = float(input("Digite sua altura: "))
  idades.append(idade)
  alturas.append(altura)
print("Idades na ordem inversa:")
for idade in reversed(idades):
  print(idade)
print("Alturas na ordem inversa:")
for altura in reversed(alturas):
  print(altura)