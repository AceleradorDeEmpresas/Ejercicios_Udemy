# Cajero Automático 

print("*** Bienvenido al cajero automático de Ciudad Gotica ***")

iniciar_operaciones = False
saldo = 5000

while not iniciar_operaciones: 
	print("""

		Menú:
		1.- Consultar Saldo
		2.- Retirar
		3.- Depositar 
		4.- Finalizar operación
	
	""")

	opcion = int(input("Selecciona una opción: "))


	if opcion == 1: 
		print(f"Tu saldo actual es de: ${saldo}.00")
	elif opcion == 2:
		cantidad_retiro = int(input("Ingrese la cantidad que desea retirar: "))
		if cantidad_retiro <= saldo:
			saldo-=cantidad_retiro
			print(f"Haz retirado: ${cantidad_retiro}.00")
		else:
			print("Lo sentimos no cuentas con fondos suficientes...")
	elif opcion == 3:
		cantidad_deposito = int(input("Ingrese la cantidad que quiere depositar: "))
		saldo+=cantidad_deposito
		print(f"Haz depositado la cantidad de: ${cantidad_deposito}.00")
	elif opcion == 4:
		print("Gracias por utilizar el cajero de Ciudad Gotica 🦇")
		iniciar_operaciones = True
	else:
		print("Lo sentimos, esa operación no existe o no esta habilitada")
