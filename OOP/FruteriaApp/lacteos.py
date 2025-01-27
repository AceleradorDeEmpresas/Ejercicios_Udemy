from tipo_producto import Tipo_Producto
class Lacteos(Tipo_Producto):
    contador_lacteo = 0
    def __init__(self, nombre, kilos):
        Lacteos.contador_lacteo += 1
        self.id_lacteo = Lacteos.contador_lacteo
        self.nombre = nombre 
        self.kilos = kilos 

    def __str__(self):
        return(f"Producto: {self.nombre} - ID: {self.id_lacteo} - Kilos: {self.kilos}")


# Código principal 
if __name__ == "__main__":
    lacteo1= Lacteos("Requeson", 1.2)
    print(lacteo1)