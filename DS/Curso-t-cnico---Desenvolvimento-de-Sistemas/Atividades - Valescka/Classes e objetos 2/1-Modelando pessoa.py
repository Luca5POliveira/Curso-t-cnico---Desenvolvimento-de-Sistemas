#1. Crie uma classe que modele uma pessoa 
#(a) Atributos: nome, idade e endereço 
#(b) Metodos: mostrar endereço e alterar endereço
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    def mostrar_endereco(self, endereco):
      print(self.endereco)
    def alterar_endereco(self, endereco):
      self.endereco = endereco
      print(self.endereco)
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
endereco = input("Digite seu endereço: ")
pessoa = Pessoa(nome, idade, endereco)
escolha = int(input("Digite 1 para mostrar endereço ou 2 para alterar endereço: "))
if escolha == 1:
    pessoa.mostrar_endereco(endereco)
elif escolha == 2:
    pessoa.alterar_endereco(endereco)