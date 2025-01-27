from tipo_producto import Tipo_Producto

class Otros_Productos(Tipo_Producto):
    contador_otro_producto = 1
    def __init__(self, nombre, producto_cat, cantidad):
        Otros_Productos.contador_otro_producto += 1
        self.id_otro_producto = Otros_Productos.contador_otro_producto
        self.nombre = nombre
        self.producto_cat = producto_cat
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto: {self.nombre} - ID: {self.id_otro_producto} - Producto: {self.producto_cat} - Cantidad: {self.cantidad}."
    

# Código principal 
if __name__ == "__main__":
    producto1 = Otros_Productos("Galletas Oreo", "Gamesa", 2)
    producto2 = Otros_Productos("Coca Cola Light", "Refresco", 1)
    producto3 = Otros_Productos("Mazapan", "Dulces", 1)

    print(producto1)
    print(producto2)
    print(producto3)
    