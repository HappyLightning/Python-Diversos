import unicodedata
import string


def shave_marks_latin(txt):
    """Remove todas as marcas de diacríticos dos caracteres-base latinos"""
    norm_txt = unicodedata.normalize('NFD', txt)  # Decompõe todos os caracteres em caracteres-base e marcas combinadas.
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:  # Pula as marcas combinadas quando o caractere-base for latino.
            continue
        keepers.append(c)  # Caso contrário, mantém o caractere atual.
        # Se não é um caractere combinado, é um novo caractere-base
        if not unicodedata.combining(c):  # Detecta o novo caractere-base e determina se é latino.
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)  # Recompõe todos os caracteres.


s = ['Café', 'Açúcar', 'Mamão', 'Peçonhento', 'Maçã']
s_shaved = [shave_marks_latin(word) for word in s]
print(s_shaved)
