# Leer la información de un archivo en Python
print("*** Leer información de un archivo  ***")

archivo = open("mi_archivo.txt", "r") # Leer archivo
print(archivo.read()) # Método read para leer la información de un archivo 

archivo.close()
