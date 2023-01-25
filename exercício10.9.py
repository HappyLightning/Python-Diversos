class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adiciona_cidade(self, cidade):
        cidade.estado = self
        self.cidades.append(cidade)

    def população(self):
        return sum([c.população for c in self.cidades])


class Cidade:
    def __init__(self, nome, população):
        self.nome = nome
        self.população = população
        self.estado = None

    def __str__(self):
        return f"Cidade (nome={self.nome}, população={self.população}, estado={self.estado})"


zanarkand = Estado("Zanarkand", "To Zanarkand")
zanarkand.adiciona_cidade(Cidade("Calm Plains", 0))
zanarkand.adiciona_cidade(Cidade("Macalania Temple", 9))
zanarkand.adiciona_cidade(Cidade("Besaid Island", 32))

kh = Estado("Kingdom Hearts", "Sora")
kh.adiciona_cidade(Cidade("Twilight Town", 1))
kh.adiciona_cidade(Cidade("Taverse Town", 7))
kh.adiciona_cidade(Cidade("Hollow Bastion", 99))

re4 = Estado("Resident Evil 4", "Forasteiro")
re4.adiciona_cidade(Cidade("Vila", 400))
re4.adiciona_cidade(Cidade("Castelo", 1016))
re4.adiciona_cidade(Cidade("Ilha", 670))

for estado in [zanarkand, kh, re4]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.população}")
    print(f"População do Estado: {estado.população()}\n")
