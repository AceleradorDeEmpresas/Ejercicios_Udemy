class Ticket: 
    contador_ticket = 0 

    def __init__(self, ordenes): 
        Ticket.contador_ticket += 1 
        self.ticket_id = Ticket.contador_ticket
        self.ordenes = ordenes 

    # Agregar ordenes a la lista  
    def agregar_orden_lista(self, orden): 
        self.ordenes.append(orden)

    def __str__(self):
        ordenes_str  = ""
        for orden in self.ordenes:
            ordenes_str += '\n' + orden.__str__()

        return f'''Ticket: {self.ticket_id}
		Orden: {ordenes_str}	
		'''
