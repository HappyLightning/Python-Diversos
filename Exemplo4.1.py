s = 'café'
print(len(s))  # a string 'cafe' tem quatro caracteres Unicode
b = s.encode()  # codificamos str para bytes usando a codificação UTF-8
print(b)
print(len(b))  # o objeto bytes na variável b tem cinco bytes (o codepoint do caracter 'é'
# é codificado com dois bytes em UTF-8
b.decode()  # decodificamos bytes para str usando a codificação UTF-8
print(b)
