#4 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
import random
vetor1 = [random.randint(0, 10) for _ in range(10)]
vetor2 = [random.randint(0, 10) for _ in range(10)]
vetor3 = [random.randint(0, 10) for _ in range(10)]
vetor4 = []
for i in range(10):
  vetor4.append(vetor1[i])
  vetor4.append(vetor2[i])
  vetor4.append(vetor3[i])
print(vetor1)
print(vetor2)
print(vetor3)
print(vetor4)
