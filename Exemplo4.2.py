cafe = bytes('café', encoding='utf_8')  # bytes pode ser construído a partir de uma str, dada uma codificação
print(cafe)
print(cafe[0])  # cada item é um inteiro em range(256)
print(cafe[:1])  # fatias de bytes também são bytes, mesmo as fatias com um único byte
cafe_arr = bytearray(cafe)
print(cafe_arr)  # não existe uma sintaxe literal para bytearray
print(cafe_arr[-1:])  # uma fatia de um bytearray também é bytearray
