#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho = float(input("Quanto você recebe por hora? "))
hora = float(input("Quantas horas você trabalhou? "))
recebimento = hora * ganho
print("Você receberá ", recebimento)