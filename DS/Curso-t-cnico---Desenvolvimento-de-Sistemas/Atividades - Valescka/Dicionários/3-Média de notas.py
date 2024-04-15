#3. Faça um programa, utilizando Dicionários, que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas.
notas = {}
for i in range(1, 5):
  nota = float(input(f"Insira a {i}ª nota: "))
  notas[f"nota{i}"] = nota
media = sum(notas.values()) / len(notas)        
print("Notas:", notas)
print("Média:", media)
