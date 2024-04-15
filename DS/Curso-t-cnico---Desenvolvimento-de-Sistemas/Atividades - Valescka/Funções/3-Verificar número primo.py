#3 - Escreva uma função chamada verifica_primo que verifica se um número é primo ou não e retorna True ou False.
def verifica_primo(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True
n = int(input("Digite o valor de n: "))
print(verifica_primo(n))