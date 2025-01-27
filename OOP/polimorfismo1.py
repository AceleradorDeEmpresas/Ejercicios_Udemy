# Polimorfismo
# Concepto: Significa multiples formas o multiples comportamientos 
# Dependiento del objeto o del tipo de dato que estemos trabajando


# Se define la clase padre Animal, tiene método hacer_sonido()
class Animal:
    def hacer_sonido(self):
        print("El animal hace sonido...")

# Se define la clase hija, Perro que hereda de la clase animal.
# se define el método hacer_sonido() para modificar el comportamiento heredaro. 
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra...")

# Se define la clase gato y se define el método hacer_sonido() para sobreescribir el método de la clase padre. 
class Gato(Animal):
    pass
    def hacer_sonido(self):
        print("El gato maulla...")


# Codigo principal se manda a imprimir el ejemplo de polimorfismo
# Se crean tres objetos, el de la clase padre y los dos objetos de las clases hijas. 
print("*** Código principal ***")

animal = Animal()
animal.hacer_sonido()

# Objeto clase hija perro 
perro = Perro()
perro.hacer_sonido()

# Objeto clase hija gato 
gato = Gato()
gato.hacer_sonido()