from carne_res import Carne_Res 
from frutas import Frutas 
from lacteos import Lacteos 
from otros_productos import Otros_Productos 
from Orden import Orden
from ticket import Ticket 

# Declaramos la variable global lista
lista = []

# Inicializamos la aplicación
def app():
    iniciar = False 
    while not iniciar:
        print("\nMenu Principal:")
        print("1. Iniciar Pedido")
        print("2. Ver Tickets")
        print("3. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            iniciar_pedido()
        if opcion == 2: 
            ver_ticket()
        elif opcion == 3:
            iniciar = True
        else: 
            print("Lo sentimos, esa opción no esta disponible")

def iniciar_pedido():
    ordenes = []
    print("\nIniciando pedido")
    while True:
        print("\nMenu Productos:")
        print("1. Carne Res")
        print("2. Frutas")
        print("3. Lacteos")
        print("4. Otros Productos")
        print("5. Agregar al Pedido")
        print("6. Finalizar Pedido")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            p_name = str(input("Tipo de carne: "))
            p_kilos = input("Cantidad: ")
            if "." in p_kilos:
                cant = float(p_kilos)
            else:
                cant = int(p_kilos)

            carne_res = Carne_Res(p_name, cant)
            ordenes.append(carne_res)
            print(carne_res)
        elif opcion == 2:
            p_name = str(input("Tipo de fruta: "))
            p_kilos = input("Cantidad: ")
            if "." in p_kilos:
                cant = float(p_kilos)
            else:
                cant = int(p_kilos)

            frutas = Frutas(p_name, cant)
            ordenes.append(frutas)
            print(frutas)
        elif opcion == 3:
            p_name = str(input("Lacteos: "))
            p_kilos = input("Cantidad: ")
            if "." in p_kilos:
                cant = float(p_kilos)
            else:
                cant = int(p_kilos)

            lacteos_sel = Lacteos(p_name, cant)
            ordenes.append(lacteos_sel)
            print(lacteos_sel)
        elif opcion == 4:
            p_name = str(input("Producto: "))
            p_cat = str(input("Categoría: "))
            p_cantidad = int(input("Cantidad: "))

            o_productos = Otros_Productos(p_name, p_cat, p_cantidad)
            ordenes.append(o_productos)
            print(o_productos)
        elif opcion == 5:
            print("\nOrdenes en el Pedido:")
            for i, orden in enumerate(ordenes):
                print(f"{i+1}. {orden}")
        elif opcion == 6:
            print("\nFinalizando Pedido")
            ticket = Ticket(ordenes)
            print(ticket)
            lista.append(ticket)
            break
        else: 
            print("Lo sentimos esa opción no existe")
        

def ver_ticket():
    print("\nTickets:")
    for i, ticket in enumerate(lista):
        print(f"{i+1}. {ticket}")


app()