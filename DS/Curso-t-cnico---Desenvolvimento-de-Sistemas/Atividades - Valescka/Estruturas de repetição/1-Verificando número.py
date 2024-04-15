#1 - Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
a = int(input("Digite uma nota de 0 a 10: "))
while a < 0 or a > 10:
  print("Número inválido")
  a = int(input("Digite uma nota de 0 a 10: "))
print("Número válido")