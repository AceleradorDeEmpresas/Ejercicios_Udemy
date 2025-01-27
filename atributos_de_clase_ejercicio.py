class Persona: 
    # Atributo de clase o variable
    contador_persona = 0

    # Constructor 
    def __init__(self, name, lastname):
        #Incrementamos el contador 
        Persona.contador_persona += 1
        self.id = Persona.contador_persona 
        self.name = name 
        self.lastname = lastname

    def mostrar_persona(self):
        print(f"Persona: ID: {self.id} - {self.name} - {self.lastname}")


# Código Principal 
print("*** Ejemplo de contador de objetos ***")

persona1 = Persona("Alex", "Aldama")
persona1.mostrar_persona()

persona2 = Persona("Monica", "Campos")
persona2.mostrar_persona()

