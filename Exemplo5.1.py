# Cria e testa uma função, em seguida, lê seu __doc__ e verifica seu tipo

def factorial(n):
    """retorna n"""
    return 1 if n < 2 else n * factorial(n-1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))
