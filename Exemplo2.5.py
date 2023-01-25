symbols = "$¤¢©³¶¿"
tuple(ord(symbol) for symbol in symbols)
import array
array.array('I', (ord(symbol) for symbol in symbols))