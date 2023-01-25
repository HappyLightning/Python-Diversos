filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"]
}
with open("filmes.html", "w", encoding="utf-8") as pg:
    pg.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
    for c, v in filmes.items():
        pg.write(f"<h1>{c}</h1>\n")
        for e in v:
            pg.write(f"<p>{e}</p>\n")
    pg.write("</body></html>")
# <ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>V