from dispositivo_entrada import DispositivoEntrada 

class Teclado():
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1 
        self.id = Teclado.contador_teclados
        self.marca = marca 
        self.tipo_entrada = tipo_entrada
    
    def __str__(self):
        return(f'ID: {self.id}, Marca: {self.marca}, Tipo de Entrada: {self.tipo_entrada}')
    

