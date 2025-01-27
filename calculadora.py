# Programa de calculadora

print("*** Calculadora de Ciudad Gotica ***")
valor_1 = valor_2 = resultado = 0
iniciar = False

while not iniciar:

	print("""
		
		1.- Sumar 
		2.- Restar 
		3.- Multiplicar
		4.- Dividir
		5.- Salir del programa
	
	""")
	valor_1 = float(input("Ingrese el primer valor: "))
	valor_2 = float(input("Ingrese el valor dos: "))
	operacion = int(input("Seleccione una operación: "))

	if operacion == 1:
		resultado = valor_1 + valor_2
		print(f"Total de {valor_1} + {valor_2} = {resultado}")
	elif operacion == 2:
		
		resultado = valor_1 - valor_2 
		print(f"Total de {valor_1} - {valor_2} = {resultado}")
	elif operacion == 3:
		resultado = valor_1 * valor_2
		print(f"Total de {valor_1} x {valor_2} = {resultado}")
	elif operacion == 4:
		resultado = valor_1 / valor_2
		print(f"Total de {valor_1} / {valor_2} = {resultado}")
	elif operacion == 5:
		print("Cerrando calculadora...")
		iniciar = True
	else:
		print("Esa función no esta habilitada")