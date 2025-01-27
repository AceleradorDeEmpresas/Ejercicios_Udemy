from pelicula import Pelicula 
from catalogo_peliculas import Catalogo_Peliculas as catalogo_peliculas
print("*** Catálogo de Películas ***")
opcion = None 
while opcion != 4:
    try:
        print("""Opciones:
        1.- Agregar película 
        2.- Listar películas 
        3.- Eliminar archivo 
        4.- Salir
        """)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1: 
            titulo = input("Ingrese el título de la película: ")
            genero = input("Ingrese el género de la película: ")
            director = input("Ingrese el director de la película: ")
            anio = input("Ingrese el año de estreno de la película: ")
            pelicula = Pelicula(titulo, genero, director, anio)
            catalogo_peliculas.agregar_pelicula(str(pelicula))
            print("Película agregada con éxito")
        elif opcion == 2:
            catalogo_peliculas.listar_peliculas()
        elif opcion == 3: 
            catalogo_peliculas.eliminar_archivo()
        elif opcion == 4: 
            print("Saliendo del programa...")
            break 
        else: 
            print("Esa opciónnoexiste")
    except Exception as e:
        print(f"Error: {e}")
        opcion = None

else: 
    print("Se cerro el programa")