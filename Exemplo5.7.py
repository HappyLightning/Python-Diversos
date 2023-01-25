fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sort = sorted(fruits, key=lambda word: word[::-1])
print(sort)