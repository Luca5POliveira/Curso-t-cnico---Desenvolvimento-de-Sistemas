#5 - Escreva uma função chamada maior_valor que aceita uma lista de números como parâmetro e retorna o maior valor na lista.
def maior_valor(lista):
  maior = lista[0]
  for i in range(1, len(lista)):
    if lista[i] > maior:
      maior = lista[i]
  return maior
lista = [10, 2, 3, 1, 5, 6]
print(maior_valor(lista))  # Saída: 10
lista = [-2, -5, -1, -3, -4]
print(maior_valor(lista))  # Saída: -1