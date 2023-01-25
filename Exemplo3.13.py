from unicodedata import name  # importa a função name para obter os nomes dos caracteres

x = {chr(i) for i in range(32, 256) if "SIGN" in name(chr(i), '')}  # ¹ Cria um conjunto de caracteres com os códigos
# ² de 32 a 255 que tenham a palavra 'SIGN' em seus nomes
print(x)
