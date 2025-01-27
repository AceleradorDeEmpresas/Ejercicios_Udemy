print("*** Herencia ***")

# Concepto de herencia

# Clase Padre
class Animal(): 
    def comer(self):
        print("Como dos veces al día") 

    def dormir(self):
        print("Duermo cuando tengo sueño")

# Clase hija en Python
class Perro(Animal):

    def hacer_sonido(self):
        print("Puedo ladrar")

    def habilidad(self):
        print("Puedo perseguir mi cola")

    # Sobreescribir un método en python 
    # Tiene que ser igual al método de la clase Padre (Mismos argumentos o parametros)
    def dormir(self):
        print("Duermo 5 horas al día")


# Objetos
animal1 = Animal()
animal1.comer()
animal1.dormir()

# Imprimir clase hija soy un perro 
perro1 = Perro()
perro1.hacer_sonido()
perro1.dormir()