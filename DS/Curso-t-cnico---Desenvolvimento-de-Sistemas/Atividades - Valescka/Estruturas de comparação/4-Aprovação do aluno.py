#4 - Faça um programa para a leitura de duas notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
notaUm = float(input("Digite a primeira nota: "))
notaDois = float(input("Digite a segunda nota: "))
media = (notaUm + notaDois) / 2
if media >= 7 and media < 10:
  print("Aprovado")
elif media < 7:
  print("Reprovado")
elif media == 10:
  print("Aprovado com Distinção")