class Pelicula: 

    def __init__(self, titulo, genero, director, anio):
        self.titulo = titulo
        self.genero = genero
        self.director = director
        self.anio = anio
        

    def __str__(self):
        return f"""
        Título: {self.titulo}
        Género: {self.genero}
        Director: {self.director}
        Año de estreno: {self.anio}
        """
