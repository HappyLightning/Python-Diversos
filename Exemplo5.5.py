def factorial(n):
    """retorna n"""
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

l = list(map(fact, range(6)))  # Cria uma lista de fatoriais de 0! a 5!
print(l)

l2 = [fact(n) for n in range(6)]  # Mesma operação com uma list comprehension
print(l2)

l3 = list(map(factorial,filter(lambda n: n % 2, range(6))))  # Lista de fatoriais de números ímpares até 5! usando map e filter
print(l3)

l4 = [factorial(n) for n in range(6) if n % 2]  # List comprehension faz a mesma tarefa substituindo map e filter e tornando
# lambda denecessario
print(l4)
