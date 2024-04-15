#7. Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). 
#Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
#Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho.pop(0)
# Criar dois macacos
macaco1 = Macaco('Juca')
macaco2 = Macaco('Chico')
# Alimentar os macacos
macaco1.comer('banana')
macaco1.comer('maçã')
macaco2.comer('laranja')
macaco2.comer('pêssego')
# Ver o conteúdo do estômago dos macacos
macaco1.verBucho()
macaco2.verBucho()
# Digerir
macaco1.digerir()
macaco2.digerir()
# Tentar fazer um macaco comer o outro
macaco1.comer(macaco2)
# Ver o conteúdo do estômago do macaco que comeu o outro
macaco1.verBucho()