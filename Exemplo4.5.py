#  String codificada com três codecs gerando sequências bem diferentes de bytes
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'Café com Açucar'.encode(codec), sep='\t')
    