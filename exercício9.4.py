import sys

# Verifica se os parâmetros foram passados
if(len(sys.argv)!=4): # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-04.py primeiro segundo saída\n\n")
else:
    primeiro = open(sys.argv[1],"r")
    segundo = open(sys.argv[2],"r")
    saída = open(sys.argv[3],"w")

    # Funciona de forma similar ao readlines
    for l1 in primeiro:
        saída.write(l1)
    for l2 in segundo:
        saída.write(l2)

    primeiro.close()
    segundo.close()
    saída.close()