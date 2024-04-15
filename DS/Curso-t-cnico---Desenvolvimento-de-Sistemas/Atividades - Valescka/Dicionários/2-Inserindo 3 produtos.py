#2. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.
produto1 = input("Escreva o nome do primeiro item: ")
preco1 = float(input("Escreva o preço do primeiro item: "))
print("Primeiro item salvo com sucesso :) ")
produto2 = input("Escreva o nome do primeiro item: ")
preco2 = float(input("Escreva o preço do primeiro item: "))
print("Segundo item salvo com sucesso :)")
produto3 = input("Escreva o nome do primeiro item: ")
preco3 = float(input("Escreva o preço do primeiro item: "))
print("Terceira item salvo com sucesso :)")
dicio_mercado = {'Produto 1': produto1, 'preço':  preco1, 'Produto 2': produto2, 'preço':  preco2, 'Produto 3': produto3, 'preço':  preco3}
print(" ")
print(dicio_mercado)