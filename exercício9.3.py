with open("pareseimpares.txt", "w") as pareseimpares:
    with open("impares.txt") as impares, open("pares.txt") as pares:
        for l in pares.readlines():
            pareseimpares.write(l)
        for x in impares.readlines():
            pareseimpares.write(l)


