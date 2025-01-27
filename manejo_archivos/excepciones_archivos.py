print("*** Excepciones y Archivos ***")

nombre_archivo = "mi_archivo.txt"
archivo = None
#Excepción
try:
    archivo = open(nombre_archivo, "a+")
    # También se pueden anidar try - excep pero no es tan necesario
    archivo.write("Nuevo contenido...")
except FileNotFoundError as e:
    print(f"Error al abrir el archivo: {e}")
else: 
    print(f"Se abrió correctamente el archivo: {nombre_archivo}")
finally:
    print("Termina programa...")
    if archivo is not None:
        archivo.close()
        print("Se cerro el recurso correctamente...")
    else: 
        print("La variable de archivo no se inicializo...")