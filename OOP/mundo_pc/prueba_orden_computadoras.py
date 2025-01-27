from monitor import Monitor 
from teclado import Teclado 
from raton import Raton 
from computadora import Computadora 
from orden import Orden 


# Creando objetos computadora 
monitor1 = Monitor("HP", 27)
teclado1 = Teclado("HP", "USB")
raton1 = Raton("HP", "USB")
computadora1 = Computadora("HP", monitor1, teclado1, raton1)

monitor2 = Monitor("Dell", 25)
teclado2 = Teclado("Dell", "Bluetooth")
raton2 = Raton("Dell", "Bluetooth")
computadora2 = Computadora("Dell", monitor2, teclado2, raton2)

# Agregando a la lista de computadoras
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)


# Vamos a agregar otras dos computadoras más 
monitor3 = Monitor("Lenovo", 22)
teclado3 = Teclado("Lenovo", "Bluetooth")
raton3 = Raton("Lenovo", "Bluetooth")
computadora3 = Computadora("Lenovo", monitor3, teclado3, raton3)

monitor4 = Monitor("Acer", 28)
teclado4 = Teclado("Acer", "Bluetooth")
raton4 = Raton("Acer", "Bluetooth")
computadora4 = Computadora("Acer", monitor4, teclado4, raton4)

orden1.agregar_computadora(computadora3)
orden1.agregar_computadora(computadora4)
print(orden1)