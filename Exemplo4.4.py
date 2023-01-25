import struct
fmt = '<3s3sHH'  # formato de struct: <little-endian; 3s3s duas sequências de 3 bytes; HH dois inteiros de 16 bits.
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())  # cria a memoryview a partir do conteúdo do arquivo em memória...
header = img[:10]  # e depois outra memoryview ao fatiar a primeira; nenhum byte é copiado nesse caso
cabeça = bytes(header)  # converte para bytes somente para exibição; 10 bytes são copiados aqui
print(cabeça)
pacote = struct.unpack(fmt, header)  # desempacota memoryview em uma tupla com: tipo, versão, largura e altura
print(pacote)
del header
del img  # apaga as referências para liberar a memória associada às instâncias de memoryview
