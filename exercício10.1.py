class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = "60 Polegadas"
        self.marca = "Samsung"


tv = Televisao()
print(tv.ligada, tv.canal, tv.tamanho, tv.marca)
# Tv da Sala
tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4
tv_sala.tamanho = "32 Polegadas"
tv_sala.marca = "LG"
print(tv_sala.ligada, tv_sala.canal, tv_sala.tamanho, tv_sala.marca)
