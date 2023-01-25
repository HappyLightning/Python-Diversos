# Ordenando uma lista de palavras de acordo com a sua grafia inversa

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']


def reverse(word):
    return word[::-1]


print(reverse('testing'))
print(sorted(fruits, key=reverse))
