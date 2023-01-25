import sys
import re
import collections

WORD_RE = re.compile('\w+')
index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            colum_no = match.start() + 1
            location = (line_no, colum_no)
            index[word].append(location)
# Exibe em ordem alfabética
for word in sorted(index, key=str.upper):
    print(word, index[word])
