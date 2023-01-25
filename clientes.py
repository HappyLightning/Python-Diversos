class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    def imprime_dados(self):
        print(f"Nome: {self.nome} Telefone: {self.telefone}")
