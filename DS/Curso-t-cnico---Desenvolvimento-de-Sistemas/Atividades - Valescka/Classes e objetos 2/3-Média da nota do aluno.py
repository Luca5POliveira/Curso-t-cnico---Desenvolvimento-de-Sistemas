#3. Crie uma classe representando os alunos de um determinado curso. 
#A classe deve conter os atributos matrícula do aluno, nome, nota da primeira prova, nota da segunda prova e nota da terceira prova. 
#Crie metodos para acessar o nome e a media do aluno. 
#(a) Permita ao usuario entrar com os dados de 5 alunos. 
#(b) Encontre o aluno com maior media geral. 
#(c) Encontre o aluno com menor media geral  
#(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para aprovação.  
class Aluno:
  def __init__(self, matricula, nome, nota1, nota2, nota3):
      self.matricula = matricula
      self.nome = nome
      self.nota1 = nota1
      self.nota2 = nota2
      self.nota3 = nota3

  def calcular_media(self):
      return (self.nota1 + self.nota2 + self.nota3) / 3

  def status_aprovacao(self):
      if self.calcular_media() >= 6:
          return "Aprovado"
      else:
          return "Reprovado"
alunos = []
for i in range(5):
  matricula = input("Matrícula do aluno {}: ".format(i+1))
  nome = input("Nome do aluno {}: ".format(i+1))
  nota1 = float(input("Nota da primeira prova do aluno {}: ".format(i+1)))
  nota2 = float(input("Nota da segunda prova do aluno {}: ".format(i+1)))
  nota3 = float(input("Nota da terceira prova do aluno {}: ".format(i+1)))
  alunos.append(Aluno(matricula, nome, nota1, nota2, nota3))

aluno_maior_media = max(alunos, key=lambda aluno: aluno.calcular_media())
print("Aluno com maior média geral:", aluno_maior_media.nome)

aluno_menor_media = min(alunos, key=lambda aluno: aluno.calcular_media())
print("Aluno com menor média geral:", aluno_menor_media.nome)

print("\nSituação de aprovação dos alunos:")
for aluno in alunos:
  print("Nome:", aluno.nome, "- Situação:", aluno.status_aprovacao())