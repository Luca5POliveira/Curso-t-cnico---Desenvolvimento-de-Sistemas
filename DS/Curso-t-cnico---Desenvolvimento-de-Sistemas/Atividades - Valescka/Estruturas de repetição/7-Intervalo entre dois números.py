#7 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
#Altere o programa anterior para mostrar no final a soma dos números.
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um outro número inteiro: "))
soma = 0
for i in range(num1+1,num2):
  print(i)
  soma = soma + i
print(soma)

