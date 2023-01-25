octets = b'Montr\xe9al'  # Bytes de "Montréal" codificados como latin1: '\xe9' é o byte para 'é'.
dec_cp1252 = octets.decode('cp1252')
print(dec_cp1252)  # Decodificar com o cp1252 (Windows 1252) funciona, pois é subconjunto de latin1.
dec_iso8859 = octets.decode('iso8859_7')
print(dec_iso8859)  # ISO-8859-7 foi criado para grego, portanto o byte é interpretado incorretamente, mas nenhum erro é gerado.
dec_koi8_r = octets.decode('koi8_r')
print(dec_koi8_r)  # KOI8-R foi criado para russo, o byte corresponde a uma letra do alfabeto cirílico.
dec_utf_8 = octets.decode("utf_8")
print(dec_utf_8)  # octets não é um UTF-8 válido e gera um UnicodeDecodeError
dec_utf_8 = octets.decode("utf_8", errors="replace")
print(dec_utf_8)  # Ao usar o tratamento de erro, '\xe9' é substituído por '?' (Em Unicode: U+FFFD), código oficial
# denominado REPLACEMENT CHARACTER cujo propósito é representar caracteres desconhecidos.
