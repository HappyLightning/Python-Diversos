import re

re_numbers_str = re.compile(r'\d+')     # As duas primeiras expressões regulares são do tipo str
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')  # As duas últimas são bytes
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"  # Texto Unicode a ser pesquisado, contendo os dígitos em tâmil para 1729
            " as 1729 = 1³ + 12³ = 9³ + 10³.")        # Essa string é unida à anterior em tempo de compilação

text_bytes = text_str.encode('utf_8')  # Uma string bytes é necessária para pesquisar com expressões regulares do tipo bytes.

print('Text', repr(text_str), sep='\n  ')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))      # o padrão str r'\d+' corresponde aos dígitos em tâmil e ASCII
print('  bytes:', re_numbers_bytes.findall(text_bytes))  # o padrão bytes rb'\d+' corresponde somente aos bytes ASCII para dígitos
print('Words')
print('  str  :', re_words_str.findall(text_str))        # o padrão str r'\w+' corresponde a letras, sobrescritos, tâmil e dígitos ASCII
print('  bytes:', re_words_bytes.findall(text_bytes))    # o padrão bytes rb'\w+' corresponde somente aos bytes ASCII para letras e dígitos
