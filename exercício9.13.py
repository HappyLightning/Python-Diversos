# Esse programa deve receber três parametros pela linha de comando: nome do arquivo, a linha inicial e a última.
import sys

if len(sys.argv) != 4:
    print("\nUso: nome nome_arqv linha_inicio linha_fim\n\n")
else:
    nome = sys.argv[1]
    linicio = int(sys.argv[2])
    lfim = int(sys.argv[3])
    arquivo = open(nome, "r")
    for linha in arquivo.readlines()[linicio - 1:lfim]:
        print(linha[:-1])  # Como a linha termina com ENTER
        # Retira-se o último caractere antes de imprimir
    arquivo.close()
