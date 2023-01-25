from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
City._fields
('name', 'country', 'population', 'coordinates')
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 24.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data) # Permite instanciar uma tupla nomeada a partir de um iterável.
delhi._asdict() # Retorna um collections.OrderedDict criado a partir da instância da tupla nomeada.
for key, value in delhi._asdict().items():
    print(key + ':', value)