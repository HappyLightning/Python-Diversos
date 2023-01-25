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


single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",  # <1>
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({  # <2>
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})
# <1> Cria tabela de mapeamento para substituição de caractere para caractere.
# <2> Cria tabela de mapeamento para substituição de caractere para string.

multi_map.update(single_map)  # Combina as tabelas de mapeamento


def dewinize(txt):
    """Substitui símbolos Win1252 por caracteres ou sequências ASCII"""
    return txt.translate(multi_map)


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)


order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'

print(dewinize(order))  # Substitui aspas curvas, bullets e 'tm' (marca registrada).
print(asciize(order))  # Aplica dewinize, remove diacríticos e substitui 'ß'
