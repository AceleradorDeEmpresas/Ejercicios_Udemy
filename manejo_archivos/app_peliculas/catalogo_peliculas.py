import os
# Clase lista películas 
class Catalogo_Peliculas:
    archivo_catalogo = "catalogo-peliculas.txt"
    @classmethod
    def agregar_pelicula(cls, pelicula):
        if os.path.exists(os.path.join(ruta, cls.archivo_catalogo)):
            os.mkdir(os.path.join(ruta, cls.archivo_catalogo))
        with open(cls.archivo_catalogo, "a", encoding="utf-8") as archivo:
            archivo.write(pelicula + "\n")
    
    @classmethod 
    def listar_peliculas(cls):
        with open(cls.archivo_catalogo, "r", encoding="utf-8") as archivo:
            print("*** Listado de Películas ***")
            print(archivo.read())

    @classmethod 
    def eliminar_archivo(cls):
        os.remove(cls.archivo_catalogo)
        print(f"Archivo {cls.archivo_catalogo} eliminado")

    

    