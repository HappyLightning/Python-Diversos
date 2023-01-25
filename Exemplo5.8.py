# Um BingoCage realiza uma única tarefa - seleciona itens de uma lista embaralhada
import random


class BingoCage:
    def __init__(self, itens):
        self._itens = list(itens)  # '__init__' aceita qualquer iterável; criar uma cópia local evita efeitos
        # colaterais inesperados em qualquer list passada como argumento.
        random.shuffle(self._itens)  # É certo que 'shuffle' funcionará porque 'self.itens' é uma list.

    def pick(self):  # O método principal
        try:
            return self._itens.pop()
        except IndexError:
            raise LookupError('Pego de uma BingoCage vazia')  # Se 'self._itens' estiver vazio


def __call__(self):  # Atalho para 'bingo.pick(): bingo()'
    return self.pick()


# Instancia
bingo = BingoCage(range(5))
print(bingo.pick())
callable(bingo)
