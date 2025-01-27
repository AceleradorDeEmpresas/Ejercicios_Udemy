# Colecciones
# Tuplas
# Lista
# Listas tipo Set
# Diccionarios 

print("*** Listas en Python ***")

nombres = [
	
	"Alejandro",
	"Monica",
	"Raúl"
	
]

# print(f"Lista de nombres: {nombres}")
# print("\n")

# Lista heterogenea (multiples tipos de datos)
# se le llama así cuando se tienen multiples tipo de datos num, str, bool
lista_heterogenea = [
	
	100, 
	True, 
	"Alex"

]

# Recorrer ls lista con ciclo for 
# for nombre in nombres:
#     print(nombre, end="  ")
    # Imprimir nombres o elementos de lista
    # en una sola linea print(nombre, end="  ") se imprimen en una misma línea con es un espacio
    

# Lista de números 
numeros = [100, 200, 300, 400, 500]

# Modificando la lista de números
numeros[0] = 3000 # Se modifica la lista números en el índice 0
numeros[4] = 10 # Se modifica la lista números en el índices 4

# print(numeros, end="-")

# Preguntar si un valor existe en la lista
numero_a_buscar = 400	 
# if numero_a_buscar in numeros:
#     print(f"Si existe el número {numero_a_buscar}")
# else:
#     print(f"El número {numero_a_buscar} no existe en la lista")
    
# Recuperar el índice de cierto elemento
# Para recuperar el índice de un elemento en una lista, se utiliza el método index()
# indice = numeros.index(numero_a_buscar)
# print(f"El índice del número {numero_a_buscar} es : {indice}")

# Redifinir lista 
numeros = [100, 200, 300, 400, 500]
# Concepto sublista 
# Al igual que las subcadenas se utiliza el mismo concepto ejemplo: valores_recuperados = numeros[valor_1:valor_3 - 1] 
# valores_recuperados = numeros[0:3]
# print(valores_recuperados)

# Recuperar sublista con el índice final
# Otra forma de recuperar una sublista es aplicando el siguiente concepto: numeros[:2]
# Esto dará como resultado: [100, 200]
valores_recuperados = numeros[:2]
print(valores_recuperados)
# Recuperar sublista con el índice de incio
# Esto dará como resultado: [400, 500]
valores_recuperados = numeros[3:]
print(valores_recuperados)

# Realizar copia de una lista 
lista_copiada = numeros[:]
# print(f"Esta es una ista copiada: {lista_copiada}")

# Métodos de listas 

# Conocer el largo de una lista con método len()
largo_lista = len(numeros)
print(largo_lista)

# Agregar nuevos elementos a la lista con el método append() agrega el nuevo elemento al final de la lista
numeros.append(800)
print(numeros)

# Insertar nuevos elementos en el índice deseado con el método insert() este método no elimina los elementos, solo los recorre
numeros.insert(2, 50)
print(numeros)


# Eliminar valor de una lista con el método  remove() sólo elimina elementos de izquierda a dercha
numeros.remove(300)
print(numeros)

# Concatenar lista 
nueva_lista = numeros + lista_copiada
print(nueva_lista)

# Eliminar elementos por índice por medido de la palabra reservada del  
del numeros[0]
print(f"Lista sin el valor del índice 0: {numeros}")

# Eliminar la lista completa 
numeros[:] = []
print(numeros)

# ELiminar por completo una variable incluidas listas
del numeros 
print(numeros)