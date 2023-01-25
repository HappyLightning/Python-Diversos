import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers) # Cria um memoryview a partir de um array de 5 shorted signed integers (typecode 'h')
print(len(memv))
print(memv[0]) # memv vê os mesmos 5 numeros do array

memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)