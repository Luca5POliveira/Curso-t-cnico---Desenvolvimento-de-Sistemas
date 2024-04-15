#2 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
import random
vetor_a = [random.randint(0, 10) for _ in range(10)]
soma_dos_quadrados = 0
for elemento in vetor_a:
  soma_dos_quadrados += elemento ** 2
print(vetor_a)
print(f"A soma dos quadrados dos elementos do vetor é: {soma_dos_quadrados}")