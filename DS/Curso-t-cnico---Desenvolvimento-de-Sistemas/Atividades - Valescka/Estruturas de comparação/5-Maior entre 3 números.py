#5 - Faça um Programa que leia três números e mostre o maior deles.
nUm = float(input("Digite o primeiro número: "))
nDois = float(input("Digite o segundo número: "))
nTres = float(input("Digite o terceiro número: "))
if nUm > nDois and nUm > nTres:
  print("O maior número é: ", nUm)
elif nDois > nUm and nDois > nTres:
  print("O maior número é: ", nDois)
elif nTres > nUm and nTres > nDois:
  print("O maior número é: ", nTres)