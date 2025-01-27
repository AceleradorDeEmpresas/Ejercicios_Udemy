# Escribir información a un archivo 
print("*** Escribir información a un archivo ***")

archivo = open("mi_archivo.txt", "w")
archivo.write("Hola mi nombre es Alejandro Aldama\n")
archivo.close() # Cerrarmos el archivo o buffer de memoria, esto es una buena practica cuando trabajamos con archivos. 
