animales = {
    "Perro": "Woof!",
    "Gato": "Meow!",
    "Cerdo": "Graz!",
    "Raton": "Squeak!"
}
# Un diccionario almacena sus elementos en forma de llave 
# valor, y además no se pueden duplicar sus elementos 

# Acceder a los elementos del diccionario 
print(f'El perro hace: {animales["Perro"]}')
#Obteniendo un valor de una llave con el método get()
print(f'¿Qué animal hace {animales.get("Gato")}?')

# Agregar nuevos elementos al diccionario 
animales["Gallo"] = "Cocoroco"

print(f"Diccionario modificado {animales}")

# Obtener una lista de todas las llaves del diccionario 
print(f"Lista de las llaves del dic: {animales.keys()}")

# Obtener una lista de los valores del diccionario 
print(f"Lista de los valores del dic: {animales.values()}")

# Obtener elementos del diccionario: items
# Esto va a retornar una tupla con los keys y valores del diccionario animales
print(f"Lista de elementos del dic: {animales.items()}")

# Verificar si existe una llave en el diccionario 
animal = "Gallo"

if animal in animales:
	print(f"La llave {animal} si existe en el dic animales")
else: 
	print(f"La llave {animal} no existe en el dic animales")

# Modificar un elemento del dic 
animales["Gallo"] = "No hace ruido"

print(f"Nuevo dic modificado: {animales}")

# Eliminar un elemento del diccionario con el método pop()
animales.pop("Gallo")
print(f"Nuevo dic: {animales}")

# Recorrer llaves de un diccionario 
for llave in animales.keys():
	print(llave, end="  ")

print("\n")
# Recorrer un item de un diccionario 
for items in animales.values():
	print(items, end="  ")

# Recorrer llave con su valor como tupla 
for llave, valor in animales.items():
	print(f"Llave: {llave}, valor: {valor}")

# Limpiar el diccionario con el método clear()
animales.clear()
print(f"Dic limpiado: {animales}")
