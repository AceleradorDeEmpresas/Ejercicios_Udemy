# Anexar información a un archivo existente
# sin sobreescribir la ya existente. 
print("*** Anexar la información a un archivo  ***")
archivo = open("mi_archivo.txt", "a")
archivo.write("\nEsta es una nueva línea de texto") 
archivo.close()
