# Apendiendo a crear archivos con Python 

nombre_archivo = "mi_archivo.txt"
# La función open es una de las principales para trabajar con archivos. 
# esta función recibe dos parametros
# 1.-  Nombre del archivo a crear
# 2.- El modo (Lectura, Anexar, Escribir, Crear), modos que se representan de la siguiente manera. 

# r -> read (leer)
# a -> append (abrir)
# w -> write (escribir)
# x -> create (crear)

archivo = open(nombre_archivo, "x")
print(f"Se creo el archivo {nombre_archivo}")
