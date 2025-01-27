# Menú Interactivo con ciclo while 


print("**** Sistema de administración de cuentas ****")

salir = False
while not salir:
	print(f"""
	Menú:
	1.- Crear cuenta
	2.- Eliminar cuenta
	3.- Salir

	""")

	opcion =  int(input("Selecciona una opción"))
	
	if opcion == 1:
		print("Creando tu cuenta...\n")
	elif opcion == 2:
		print("Eliminando tu cuenta...\n")
	elif opcion == 3:
		print("Saliendo del menú...\n")
		salir = True
	else:
		print("Lo sentimos esa opción no es válida...")

