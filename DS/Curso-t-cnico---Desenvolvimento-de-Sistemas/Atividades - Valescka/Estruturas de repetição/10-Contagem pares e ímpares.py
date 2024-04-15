#10 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
count_par = 0
count_impar = 0
for i in range(10):
  num = int(input("digite um numero: "))
  if num % 2 == 0:
    count_par += 1
  else:
    count_impar += 1
print("A quantidade de numeros pares é:", count_par)
print("A quantidade de numeros impares é:", count_impar)