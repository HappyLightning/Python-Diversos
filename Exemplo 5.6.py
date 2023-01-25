from functools import reduce
from operator import add # Importa add para evitar a criação de uma função somente para somar dois números

x = reduce(add, range(100)) # Soma inteiros até 99
print(x)

sum(range(100)) # Mesma tarefa usando sum; importação ou função para adição não são necessárias