filmes = {
    "Drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "Comédia": ["Tempos Modernos", "American Pie", "Dr. Doolittle"],
    "Policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "Guerra": ["Rambo", "Platoon", "Tora! Tora! Tora!"]
}
with open("filmes2.html", "w", encoding="utf-8") as pg:
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
        pg.write(f"<ul>\n<h1>{c}</h1>\n")
        for e in v:
            pg.write(f"<li>{e}</li>\n")
        pg.write(f"</ul>\n")
    pg.write("</body></html>")
