class Cliente:
    # Relación entre objetos clase 
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia
    
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Membresía: {self.membresia}"