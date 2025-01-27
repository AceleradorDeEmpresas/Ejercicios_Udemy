# Colección de tipo set
print("*** Manejo de set en Python ***")

# Un set es una colección desordenada de elementos únicos. Los sets no permiten elementos duplicados.
conjunto = {"Karla", 100,"Laura", 100, True}

for val in conjunto:
    print(val, end="  ")

# Las coleciones en set si se pueden eliminar elementos y agregar 
conjunto.remove(True)
print(conjunto)

# Agregar elementos con el método add()
conjunto.add("Chop")
print(conjunto)