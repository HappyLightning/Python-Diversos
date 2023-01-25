Largura = 79
with open("entrada.txt") as entrada:
    for l in entrada.readlines():
        if l[0] == ";":
            continue
        elif l[0] == ">":
            print(l[1:].rjust(Largura))
        elif l[0] == "*":
            print(l[1:].center(Largura))
        elif l[0] == "=":
            print(40*"=")
        elif l[0] == ".":
            input("Digite Enter para continuar...")
        else:
            print(l)
