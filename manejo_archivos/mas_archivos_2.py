# Otros modos de trabajar con archivos 
import os 
# r+ -> Lectura y escritura 
# w+ -> Lectura y escritura, si el archivo ya existe se sobreescribe y si no exste se crea uno nuevo 
# a+ -> Lectura y agregar, si el archivo no existe se crea para escritura. 

# Escribir una lista de datos a un archivo 
nombre_archivo = "mi_archivo.txt"
lista = ["Alex\n", "Monica\n", "Kaleth\n"]

with open(nombre_archivo, "a+") as archivo: 
	archivo.writelines(lista)
print("Se anexo la lista de datos")

# Como eliminar un archivo 
if os.path.exists(nombre_archivo):
	os.remove(nombre_archivo)
	print(f"Se elimino el archivo: {nombre_archivo}")
else:
	print(f"Archivo no encontrado: {nombre_archivo}")