# Creas lase Persona 
# Se define el constructor __init__(self, nombre, apellido):
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre 
        self.apellido = apellido

    def __str__(self):
        return f'''
            Persona: 
                Nombre: {self.nombre}
                Apellido: {self.apellido}
                Dir. mem.: {super.__str__(self)}
        '''

# Sobreescribir el métdo __str__
# def __str__(self):



# Código principal creamos objeto tipo persona
# no es necesario a mandar llamar un método mágico,
# ya que lo hacen de manera automática al instanciar una clase. 
persona1  = Persona("Alejandro", "Aldama")
print(persona1)
