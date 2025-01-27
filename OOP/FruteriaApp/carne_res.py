from tipo_producto import Tipo_Producto

class Carne_Res(Tipo_Producto): 
    contador_carne = 0

    def __init__(self, nombre, kilos):
        Carne_Res.contador_carne += 1
        self.id_carne = Carne_Res.contador_carne
        self.nombre = nombre
        self.kilos = kilos

    def __str__(self):
        return (f"Producto: {self.nombre} - ID: {self.id_carne} - Kilos: {self.kilos}kg.")
    
# Código Principal de Prueba
if __name__ == "__main__":
    carne1 = Carne_Res("Arrachera", 10)
    carne2 = Carne_Res("Diesmillo", 1)
    print(carne1)
    print(carne2)
