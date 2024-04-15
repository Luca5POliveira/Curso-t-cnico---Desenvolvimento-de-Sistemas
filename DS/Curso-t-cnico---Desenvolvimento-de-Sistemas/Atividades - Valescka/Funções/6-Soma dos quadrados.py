#7 - Escreva uma função chamada soma_quadrados que aceita uma lista de números como parâmetro e retorna a soma dos quadrados desses números.
def soma_quadrados(lista):
  soma = 0
  for i in range(len(lista)):
    soma += lista[i] ** 2
  return soma
lista = [1, 2, 3, 4, 5]
print(soma_quadrados(lista))  
lista = [-2, -5, -2, -3, -4]
print(soma_quadrados(lista)) 