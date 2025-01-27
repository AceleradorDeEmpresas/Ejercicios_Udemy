from carne_res import Carne_Res
from lacteos import Lacteos 
from frutas import Frutas 
from otros_productos import Otros_Productos 

class Orden: 
    contador_orden = 1 
    def __init__(self, carne = "", fruta = "", lacteos = "", otros_productos = ""):
        Orden.contador_orden += 1
        self.id_orden = Orden.contador_orden
        self.carne = carne
        self.fruta = fruta
        self.lacteos = lacteos
        self.otros_productos = otros_productos

    def __str__(self):
        return f"""Orden ID: {self.id_orden} 
        {self.carne}
        {self.fruta}
        {self.lacteos}
        {self.otros_productos}
        """


# Código principal
if __name__ == "__main__":
    carne1 = Carne_Res("Costilla Cargada", 2)
    orden1 = Orden(carne1)
    print(orden1)

    carne2 = Carne_Res("Carne molida", 1.2)
    lacteos2 = Lacteos("Asadero", 1)
    orden2 = Orden(carne2, lacteos2)
    print(orden2)

    carne3 = Carne_Res("Carne molida", 3)
    lacteos3 = Lacteos("Queso menonita", 1.5)
    fruta3 = Lacteos("Melón", 1.2)
    otro_producto = Otros_Productos("Leche 1lt", "Lala" ,1)
    orden3 = Orden(carne3, lacteos3, fruta3, otro_producto)
    print(orden3)
