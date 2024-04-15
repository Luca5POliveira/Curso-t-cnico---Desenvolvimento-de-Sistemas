#3 - Faça um Programa que leia dois vetores com 10 elementos cada. 
#Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
vetor_1 = []
vetor_2 = []
vetor_3 = []
for i in range(10):
  valor_1 = int(input("Digite o valor para o vetor 1: "))
  valor_2 = int(input("Digite o valor para o vetor 2: "))
  vetor_1.append(valor_1)
  vetor_2.append(valor_2)
for i in range(10):
  vetor_3.append(vetor_1[i])
  vetor_3.append(vetor_2[i])
print("Vetor 1:", vetor_1)
print("Vetor 2:", vetor_2)
print("Vetor 3:", vetor_3)
