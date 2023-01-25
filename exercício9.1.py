import sys
# Verifica se o parâmetro foi passado
if(len(sys.argv)!=2): # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: exercício9.1.py nome_do_arquivo\n\n")
else:
    nome = sys.argv[1]
    arquivo = open(nome,"r")
    for linha in arquivo.readlines():
        print(linha[:-1]) # Como a linha termina com enter,
                          # retiramos o último caractere antes de imprimir
    arquivo.close()