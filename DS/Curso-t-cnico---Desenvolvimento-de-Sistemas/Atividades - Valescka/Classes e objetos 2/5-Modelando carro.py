#5. Crie uma classe que modele um carro 
#(a) Atributos: marca, ano e preco 
#(b) Metodos: mostrar preco e de exibicao dos dados  
class Carro:
  def __init__(self, marca, ano, preco):
    self.marca = marca
    self.ano = ano
    self.preco = preco

  def mostrar_preco(self):
    print(f"O preço do carro é R${self.preco}")

  def exibir_dados(self):
    print(f"Marca: {self.marca}")
    print(f"Ano: {self.ano}")
    print(f"Preço: R${self.preco}")

# Criar um objeto da classe Carro
carro = Carro("Volkswagen", 2023, 100000)

# Mostrar o preço do carro
carro.mostrar_preco()

# Exibir os dados do carro
carro.exibir_dados()
