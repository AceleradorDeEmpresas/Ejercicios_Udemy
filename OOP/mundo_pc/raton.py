from dispositivo_entrada import DispositivoEntrada

#Creamos la clase hija ratón y extendemos la clase padre DispoSitivoEntrada
class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)
        
    def __str__(self):
        return (f'ID: {self.id_raton} Marca: {self.marca}, Tipo: {self.tipo_entrada}')
	
