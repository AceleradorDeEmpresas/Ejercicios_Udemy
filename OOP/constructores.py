class Persona: 

    def __init__(self, nombre, apellido):
        self.nombre = nombre 
        self.apellido = apellido
    
    def mostrar_persona(self):
        print(f'Persona: nombre = {self.nombre}, apellido = {self.apellido}')

persona_1 = Persona('Alejandro', 'Aldama')
persona_1.mostrar_persona()
