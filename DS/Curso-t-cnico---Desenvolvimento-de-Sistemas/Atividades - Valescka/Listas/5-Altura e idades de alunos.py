#5 - Foram anotadas as idades e alturas de 10 alunos. 
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
idades = []
alturas = []
for i in range(10):
  idade = int(input("Digite a idade do aluno: "))
  altura = float(input("Digite a altura do aluno: "))
  idades.append(idade)
  alturas.append(altura)
media_altura = sum(alturas) / len(alturas)
#alunos acima 13 anos abaixo media
x = 0
for i in range(10):
  if idades[i] > 13 and alturas[i] < media_altura:
    x += 1
print("Todas as idades dos alunos: ", idades)
print("Todas as alturas dos alunos: ", alturas)
print("A media das idades é: ", media_altura)
print(f"Existem {x} alunos com mais de 13 anos e altura inferior à média de altura.")