#2. Crie uma classe que modele uma aluno 
#(a) Atributos: nome, numero de matrıcula e curso 
#(b) Metodos: mostrar curso e alterar curso 
class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    def mostrar_curso(self, curso):
      print(self.curso)
    def alterar_curso(self, novo_curso):
      self.curso = novo_curso
nome = input("Digite o nome do aluno: ")
matricula = int(input("Digite a matricula do aluno: "))
curso = input("Digite o curso do aluno: ")
aluno = Aluno(nome, matricula, curso)
escolha = int(input("Digite 1 para mostrar curso ou 2 para alterar curso: "))
if escolha == 1:
    aluno.mostrar_curso(curso)
elif escolha == 2:
    novo_curso = input("Digite o novo curso: ")
    aluno.alterar_curso(novo_curso)