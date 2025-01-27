from cliente_dao import Cliente_Dao
from cliente import Cliente
print("*** Clientes de Zona Fit ***")

opcion = None 
while opcion != 5:
    print("""Menú:
          1.- Listar Clientes
          2.- Agregar Cliente
          3.- Modificar Cliente
          4.- Eliminar Cliente
          5.- Salir""")
    
    opcion = int(input("Escribe tu opción (1-5): )"))
    if opcion == 1: #Listar Clientes 
        clientes = Cliente_Dao.seleccionar()
        print("\n*** Listado de clientes ***")
        for cliente in clientes:
            print(cliente)
        print()
    elif opcion == 2: #Agregar Cliente
        nombre_var = input("Escribe el nombre del cliente: ")
        apellido_var = input("Escribe el apellido del cliente: ")
        membresia_var = input("Escribe el número de la membresía: ")

        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)

        clientes_insertados = Cliente_Dao.insertar(cliente)
        print(f"Clientes insertados: {clientes_insertados}\n")
    elif opcion == 3:
        id_cliente_var = int(input("Escribe el ID del cliente a modificar: "))
        nombre_var = input("Escribe el nombre del cliente: ")
        apellido_var = input("Escribe el apellido del cliente: ")
        membresia_var = input("Escribe el número de la membresía: ")
        
        cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        clientes_actualizados = Cliente_Dao.actualizar(cliente)
        print(f"Clientes actualizados: {clientes_actualizados}\n")
    elif opcion == 4:
        id_cliente_var = int(input("Escribe el ID del cliente a eliminar: "))
        cliente = Cliente(id_cliente_var)
        clientes_eliminados = Cliente_Dao.eliminar(cliente)
        print(f"Clientes eliminados: {clientes_eliminados}\n")
else:
    print("Salimos de la aplicación...")
