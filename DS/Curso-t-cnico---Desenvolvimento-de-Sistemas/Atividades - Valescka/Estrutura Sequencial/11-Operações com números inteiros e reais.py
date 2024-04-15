#11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo, a soma do triplo do primeiro com o terceiro, o terceiro elevado ao cubo.
a = int(input("Digite um numero inteiro: "))
b = int(input("Digite outro numero inteiro: "))
c = float(input("Digite um numero real: "))
d = (a * 2) * (b / 2)
e = (a * 3) + c
f = c**3
print("O produto do dobro do primeiro com metade do segundo é: ", d)
print("A soma do triplo do primeiro com o terceiro é: ", e)
print("O terceiro elevado ao cubo é: ", f) 