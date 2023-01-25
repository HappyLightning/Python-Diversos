import sys

if len(sys.argv)<2:
    print("\nUso: e09-09.py arquivo1 [arquivo2 arquivo3 arquivoN]\n\n\n")
    sys.exit(1)

for nome in sys.argv[1:]:
    arquivo = open(nome, "r")
    for linha in arquivo:
        print(linha,end="")
    arquivo.close()