# Bobo sabe que hello exige um argumento person e o obtém da requisição HTTP
import bobo
@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person