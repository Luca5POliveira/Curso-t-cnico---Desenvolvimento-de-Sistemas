#4. Faça um programa, utilizando Dicionários, que:
#1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .
#2° Passo: Peça para o usuário inserir um número.
#3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.
caixa_misteriosa = {}
for i in range(4):
  caixa = input("Insira uma coisa na caixa: ")
  caixa_misteriosa[i+1] = caixa
posicao = int(input("Digite o numero da posicao: "))
print(caixa_misteriosa[posicao])