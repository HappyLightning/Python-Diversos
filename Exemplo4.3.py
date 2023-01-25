import array

numbers = array.array('h', [-2, -1, 0, 1, 2])  # o typecode 'h' cria um array de short integers (16 bits)
octets = bytes(numbers)  # octets armazena uma cópia de short integers (16 bits)
print(octets)  # esses são os 10 bytes que representam os 5 short integers
