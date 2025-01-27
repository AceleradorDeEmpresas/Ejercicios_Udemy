class Monitor():
    contador_monitores = 0 
    
    def __init__(self, marca, size):
        Monitor.contador_monitores +=1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca 
        self.size = size 


    def __str__(self): 
        return (f'ID: {self.id_monitor}, Marca: {self.marca}, Size: {self.size}')
    