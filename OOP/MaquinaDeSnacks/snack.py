class Snack: 
    contador_de_snack = 0 

    def __init__(self, nombre, precio):
        Snack.contador_de_snack += 1
        self.id = Snack.contador_de_snack
        self.nombre = nombre
        self.precio = precio

    def __str__(self): 
        return f"""ID: {self.id} - Nombre: {self.nombre} - 
        Precio: ${self.precio}"""