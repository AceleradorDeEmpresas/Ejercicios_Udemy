# Tuplas 
print("***  Tuplas - Python  *** ")
# Una tupla es una lista que no puede ser modificada como si se puede hacer con las listas.  

# Tupla nombre
nombres = (
    "Alex", 
    "Raúl", 
    "Monica"
)

print(nombres)

# Tupla Heterogenea, que se pueden tener distintos tipos de datos. Las tuplas también pueden representarse por comas en lugar de los parentesis
heterogenea = (
    100, 
    True, 
    "Manuel"
)
print(heterogenea)
#Recorriendo elementos de una tupla con ciclo for 
for val in heterogenea:
    pass # Esta palabra reservada significa que no hay bloques de código ayuda a omitir el bloque de codigo del ciclo 

# Tupla numerica 
numeros = (100, 200, 300, 400, 500)
print(f"Para el índice 0, el valor es: {numeros[0]}")
# Tupla con indices negativos - al poner valores negativos por ejemplo -1 se recuperara el ultimo valor de la tupla o una lista, y así sucesivamente.
print(f"Recuperando el valor de -1: {numeros[-1]}")

# Buscando un valor o elemento dentro de una tupla 
if 900 in numeros:
    print("El valor si existe en la tupla")
else: 
    print("El valor no existe en la tupla")