#12 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa que gere a série até que o valor seja maior que 500.
f1 = 0
f2 = 1
while f1 <= 500:
  print(f1)
  f3 = f1 + f2
  f1 = f2
  f2 = f3