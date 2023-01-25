import unicodedata
import re


re_digit = re.compile(r'\d')
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
for char in sample:
    print('U+%04x' % ord(char),  # código Unicode no formato U+0000
          char.center(6),  # caracter centralizado numa str de tamanho 6
          're_dig' if re_digit.match(char) else '-',  # mostra re_dig se o caractere corresponde à regex r'\d'
          'isdig' if char.isdigit() else '-',  # mostra isdig se char.isdigit() for True
          'isnum' if char.isnumeric() else '-',  # mostra isnum se char.isnumeric() for True
          format(unicodedata.numeric(char), '5.2f'),  # valor formatado com largura 5 e duas casas decimais
          unicodedata.name(char),  # nome do caractere Unicode
          sep='\t')
