"""Cria um índice que mapeia palavra -> lista de ocorrências"""

import sys
import re

WORD_RE = re.compile('\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            colum_no = match.start()+1
            location = (line_no, colum_no)
            # Isto não é elegante; foi codificado desta forma para ilustrar uma questão
            ocurrences = index.get(word, [])
            ocurrences.append(location)
            index[word] = ocurrences
# Exibe em ordem alfabética
for word in sorted(index, key=str.upper):
    print(word, index[word])
"""Cria um índice que mapeia palavra -> lista de ocorrências"""

import sys
import re

WORD_RE = re.compile('\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            colum_no = match.start()+1
            location = (line_no, colum_no)
            # Isto não é elegante; foi codificado desta forma para ilustrar uma questão
            ocurrences = index.get(word, [])
            ocurrences.append(location)
            index[word] = ocurrences
# Exibe em ordem alfabética
for word in sorted(index, key=str.upper):
    print(word, index[word])
