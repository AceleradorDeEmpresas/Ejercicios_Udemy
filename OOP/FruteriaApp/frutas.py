from tipo_producto import Tipo_Producto
class Frutas(Tipo_Producto): 
    contador_fruta = 0
    def __init__(self, nombre, kilos):
        Frutas.contador_fruta += 1
        self.id_fruta = Frutas.contador_fruta
        self.nombre = nombre
        self.kilos = kilos

    def __str__(self):
        return(f"Producto: {self.nombre} - ID: {self.id_fruta} - Kilos: {self.kilos}")
    
# Codigo principal 
if __name__ == "__main__":
    fruta1 = Frutas("Manzana", 2)
    fruta2 = Frutas("Naranja", 3)
    print(fruta1)
    print(fruta2)