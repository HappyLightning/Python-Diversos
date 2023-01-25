with open("pares.txt","r") as pares, open("pares_invertido.txt","w") as saída:
    L = pares.readlines()
    L.reverse()
    for l in L:
        saída.write(l)