# Crie uma classe para implementar uma conta corrente. 
#A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
#Os métodos são os seguintes: alterarNome, depósito e saque; 
#No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
class ContaCorrente:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    def alterarNome(self, novo_nome):
        self.nome = novo_nome
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")
# Criação de uma conta corrente
conta = ContaCorrente(123, "João Silva", 1000)
# Alterar o nome do correntista
conta.alterarNome("Maria Souza")
# Depositar dinheiro
conta.deposito(500)
# Sacar dinheiro
conta.saque(200)
# Imprimir o saldo da conta
print(conta.saldo)
