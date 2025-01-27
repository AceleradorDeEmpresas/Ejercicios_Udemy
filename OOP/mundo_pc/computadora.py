# Importamos las clases 
from teclado import Teclado 
from raton import Raton 
from monitor import Monitor 


class Computadora: 
	# Creamor el atributo de tipo clase contador
    contador_computadoras = 0

	# Creamos el constructor 
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

	# Definimos el método str con una cadema multilinea
    def __str__(self):
        return f'''{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''
    

# Código principal 
# Esta comprobación hace que este código sólo se ejecute en este archivo
if __name__ == "__main__":
    teclado1 = Teclado("HP", "USB")
    raton1 = Raton("HP", "USB")
    monitor1 = Monitor("HP", 27)
    computadora1 = Computadora("HP", monitor1, teclado1, raton1)
    print(computadora1)