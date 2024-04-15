#6. Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#Atributos: Nome, Fome, Saúde e Idade b. 
#Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
#Obs: Existe mais uma informação que devemos levar em consideração:
#o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado
#então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
class Tamagushi:
  def __init__(self, nome, fome, saude, idade):
    self.nome = nome
    self.fome = fome
    self.saude = saude
    self.idade = idade

  def alterar_nome(self, novo_nome):
    self.nome = novo_nome

  def alterar_fome(self, nova_fome):
    self.fome = nova_fome

  def alterar_saude(self, nova_saude):
    self.saude = nova_saude

  def alterar_idade(self, nova_idade):
    self.idade = nova_idade

  def retornar_nome(self):
    return self.nome

  def retornar_fome(self):
    return self.fome

  def retornar_saude(self):
    return self.saude

  def retornar_idade(self):
    return self.idade

  def retornar_humor(self):
    if self.fome < 3 and self.saude > 7:
      return "Feliz"
    elif self.fome > 5 and self.saude < 5:
      return "Triste"
    else:
      return "Neutro"
# Criar um objeto da classe Tamagushi
tamagushi = Tamagushi("Tama", 2, 8, 1)
# Alterar o nome do tamagushi
tamagushi.alterar_nome("cleitinho")
# Mostrar o nome do tamagushi
print(tamagushi.retornar_nome())
# Mostrar o humor do tamagushi
print(tamagushi.retornar_humor())