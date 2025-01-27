print("***  Argumentos variables ***")


# *args hace referencia a argumentos variables
# *args -> arguments -> tupla
# **kwargs -> keyword arguments -> diccionario
def super_heroe(nombre, *args, **kwargs):
    print(f"Superheroe: {nombre} - {args} Más info: {kwargs}")

# Llamamos a la función
super_heroe("Spiderman", "Instinto aracnido", "Trepar paredes", "Lanzar telaraña")
    
# Es opcional enviar argumentos variables a una función
super_heroe("Homero Simpsom", habito="Beber cerveza")
