import unicodedata
import string


def shave_marks(txt):
    """Remove todas as marcas de diacríticos"""
    norm_txt = unicodedata.normalize('NFD', txt)  # Decompõe todos os caracteres em caracteres-base e marcas combinadas
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))  # Filtra todas as marcas combinadas.
    return unicodedata.normalize('NFC', shaved)  # Recompõe todos os caracteres.
