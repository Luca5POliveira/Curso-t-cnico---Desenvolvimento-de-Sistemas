#11 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa capaz de gerar a série até o n−ésimo termo.
n = int(input("Digite a quantidade de termos: "))
f1 = 0
f2 = 1
if n <= 1:
  print("Quantidade invalida")
else:
  print("Sequencia de Fibonacci:")
  for i in range(n):
    print(f1)
    f3 = f1 + f2
    f1 = f2
    f2 = f3
