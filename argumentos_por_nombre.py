# Argumentos por nombre 
print("*** Argumentos por nombre ***")

def crear_persona( nombre, apellido='', edad=0):
	print(f"Persona: nombre = {nombre}, apellido: {apellido}, edad: {edad}")

# Llamamos la función 
crear_persona("Alejandro", "Aldama", 37)
crear_persona("Monica")

# llamar a la función por argumentos por nombre	
crear_persona(edad=40, nombre="Raquel")
