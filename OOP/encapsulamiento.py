# Encapsulamiento
class Persona: 

    def __init__(self, nombre, apellido):
        self._nombre = nombre  # Atributo protegido añadiendo _ despues del punto (no es buena practica)
        self.__apellido = apellido # Doble __ se conoce como atributo privado

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido
        
    
    def mostrar_persona(self):
        print(f'Persona: nombre = {self._nombre}, apellido = {self.__apellido}')



persona_1 = Persona('Alejandro', 'Aldama')

#Lectura de los atributos
print(persona_1.get_nombre())
print(persona_1.get_apellido())

#Modificar atributos nombre y apellido 
persona_1.set_nombre("Monica")
persona_1.set_apellido("Campos")
persona_1.mostrar_persona()


