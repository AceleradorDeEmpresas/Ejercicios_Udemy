from modulo_funcion import recibir_mensaje
# Funciones python 
print("*** Funciones en Python ***")
# Divide y venceras
# Una función nos permite dividir nuestro código en un
# de manera que un programa muy grande los podemos dividir 
# en partes más pequeñas, a esto se le llama modularidad.
# Beneficios de las funciones es que podemos reutilizar nuestro código 
# una función es un bloque de código que realiza una tarea en particular 

# Enviar información a una función
argumento = input("Ingresa un mensaje: ")
mensaje = recibir_mensaje(argumento)
print(mensaje)
