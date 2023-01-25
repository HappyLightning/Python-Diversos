# Listando os atributos de funções que não existem em instâncias simples
class C:
    pass  # Cria uma classe vazia definida pelo usuário


obj = C()


def func(): pass  # Função vazia


lista = sorted(set(dir(func)) - set(dir(obj)))
# Usando a diferença entre conjuntos, gera uma lista ordenada de atributos existentes
# em uma função, mas não em uma instância de uma classe vazia.
print(lista)
