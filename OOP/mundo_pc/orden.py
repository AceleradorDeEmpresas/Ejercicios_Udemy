# Se crea la clase Orden 
class Orden: 

	# Se crea el atributo de clase contador de orden 
	contador_orden = 0 
	# Se crea el constructor de orden  
	def __init__(self, computadoras):
		# Recibimos una lista de objetos Computadoras
		Orden.contador_orden += 1	
		self.id_orden = Orden.contador_orden
		self.computadoras = computadoras
	# Agregamos a la lista de objetos Computadoras
	def agregar_computadora(self, computadora):
		self.computadoras.append(computadora)
	# Se crea el método __str__
	def __str__(self):
		computadoras_str = ''
		for computadora in self.computadoras:
			computadoras_str += '\n' + computadora.__str__()

		return f'''Orden: {self.id_orden}
		Computadoras: {computadoras_str}	
		'''