#2 - Escreva uma função chamada fatorial que calcula o fatorial de um número inteiro fornecido como argumento.
def fatorial(n):
  fat = 1
  for i in range(1, n + 1):
    fat *= i
  return fat
n = int(input("Digite o valor de n: "))
print(fatorial(n))
