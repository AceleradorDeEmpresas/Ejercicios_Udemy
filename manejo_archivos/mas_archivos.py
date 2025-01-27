# Como leer lineas de un archivo 

nombre_archivo = "mi_archivo.txt"

archivo = open(nombre_archivo) # Si no se especifica un modo en el segundo parametro, se abre en modo lectura "r"


# Leer todas las lineas del archivo 
for linea in archivo: 
	print(linea)



archivo = open(nombre_archivo)
lineas = archivo.readlines()
for linea in lineas:
	print(linea)
archivo.close()

# Abrir el archivo como recurso usando la palabra reservada  (with)
# Esta instrucción permite abrir el archivo como cerrarlo
# Esta última opción es la forma recomendada de trabajar con nuestros archivos
# Ya que si olvidamos cerrar el archivo, esa instrucción lo hace autómaticamente 
with open(nombre_archivo) as archivo:
	print(archivo.read())
