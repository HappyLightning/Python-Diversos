class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abre_conta(self, conta):
        self.contas.append(conta)

    def lista_contas(self):
        print(f"Lista de contas do banco {self.nome}:\n")
        for c in self.contas:
            c.resumo()
        print(160 * "*")
