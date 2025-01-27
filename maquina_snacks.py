print("*** Máquina de snacks ***")
#Dir productos 
productos = [
    {
        "id": 0,
        "Nombre": "Papas Pringles",
        "Precio": 20 
    },
    {
        "id": 1,
        "Nombre": "Gansito",
        "Precio": 16
    },
    {
        "id": 2,
        "Nombre": "Donitas Bimbo",
        "Precio": 25
    },
    {
        "id": 3,
        "Nombre": "Doritos",
        "Precio": 20
    }
]
# Variable que almacena los productos seleccionados por el usuario
selected_products = []

print("*** Snacks Disponibles ***")
for snack_list in productos:
    print(  f"ID: {snack_list['id']} -> "
            f"Nombre: {snack_list['Nombre']} -> "
            f"Precio: {snack_list['Precio']} ")


# Función que inicializa la máquina de snacks
def maquina_de_snacks(productos, selected_products):
    iniciar = True
    while iniciar:
        print("""
            Menú:
                1. Comprar snack
                2. Mostar ticket
                3. Salir
        """)
        opcion = int(input("Escoge una opción: "))

        # Evaluar opción seleccionada 
        if opcion == 1:
            comprar_producto(productos, selected_products)

        elif opcion == 2:
            # Se manda a llamar la función de generar total 
            mostrar_ticket(selected_products)

        elif opcion == 3:
            print("Gracias por comprar en nuestras máquinas vending machine, ¡vuelva pronto!")
            iniciar = False
        else:
            print("Lo sentimos esa opción no existe, intente de nuevo")

# Función comprar producto 
def comprar_producto(productos, selected_products):
    id_snack = int(input("¿Qué snack quieres (id)?: "))
    selected_products.append(productos[id_snack])
    for producto in selected_products:
        print(f"Haz agregado el producto: {producto}")
    

# Función para generar el total de productos seleccionados
def mostrar_ticket(selected_products):
    ticket = f"\t*** Ticket de venta ***"
    total = 0
    for producto in selected_products:
        ticket += f"\n\t- {producto['Nombre']} - ${producto['Precio']}.00"
        total += producto["Precio"]

    ticket += f"\n\tTotal: ${total}.00"
    print(ticket)

#Invocamos la función máquina de snacks
maquina_de_snacks(productos, selected_products)