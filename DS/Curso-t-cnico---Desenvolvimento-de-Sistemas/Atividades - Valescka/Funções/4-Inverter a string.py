#4 - Escreva uma função chamada inverte_string que aceita uma string como parâmetro e retorna a string invertida.
def inverte_string(s):
  invertida = ""
  for i in range(len(s) - 1, -1, -1):
    invertida += s[i]
  return invertida
s = input("Digite a frase ou palavra: ")
print(inverte_string(s))