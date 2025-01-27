print("*** Regresar una tupla de valores desde una función ***")

def persona_mayusculas(nombre, apellido, edad):
	print("Esta función regresa varios valores (tupla)")
	# tupla
	return nombre.upper(), apellido.upper(), edad

nombre, apellido, edad = persona_mayusculas('monica', 'campos', 31)

print(f"Persona: nombre = {nombre}, apellido: {apellido}, edad: {edad}")

