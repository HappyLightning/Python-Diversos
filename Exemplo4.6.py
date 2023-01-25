#  Codificação para bytes com tratamento de erro
city = 'São Paulo'
# As codificações utf tratam qualquer str.
print(city.encode('utf_8'))
print(city.encode('utf_16'))
# Também funciona para str 'São Paulo'.
print(city.encode('iso8859_1'))
# Não consegue codificar 'ã', o tratamento do erro deafult-'strict' gera UnicodeEncodeError.
print(city.encode('cp437'))
# O tratamento descarta silenciosamente os caracteres que não podem ser codificados.
print(city.encode('cp437', errors='ignore'))
# Substitui os caracteres que não podem ser codificados por '?', dados são perdidos.
print(city.encode('cp437', errors='replace'))
# Substitui caracteres que não podem ser codificados por uma entidade XML.
print(city.encode('cp437', errors='xmlcharrefreplace'))
