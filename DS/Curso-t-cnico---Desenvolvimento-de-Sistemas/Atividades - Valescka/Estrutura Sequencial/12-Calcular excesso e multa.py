#12 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
#João precisa que você faça um programa que leia a variável  (peso de peixes) e calcule o excesso. 
#Gravar na variável  a quantidade de quilos além do limite e na variável  o valor da multa que João deverá pagar. 
#Imprima os dados do programa com as mensagens adequadas.
peso_peixes = float(input("Qual o peso dos peixes? "))
if peso_peixes > 50:
    excesso = peso_peixes - 50
    multa = excesso * 4
    print("O peso excedente é de", excesso, "kg")
    print("O valor da multa é de R$", multa)
else:
    print("O peso dos peixes está dentro do limite permitido.")
