from snack import Snack
from snacks import Snacks

# Lista de productos (vacia)
productos = []

print('*** Maquina de Snacks ***')
print('Snacks Disponibles:')
snacks = Snacks()
print(snacks)

def maquina_snacks(snacks, productos):
    salir = False
    while not salir:
        print(f'''Menu:
        1. Comprar snack
        2. Mostrar ticket
        3. Agregar Snack
        4. Salir''')
        opcion = int(input('Escoge una opcion: '))
        if opcion == 1:
            comprar_producto(snacks, productos)
        elif opcion == 2:
            mostrar_ticket(productos)
        elif opcion == 3:
            agregar_snack(snacks)
        elif opcion == 4:
            print('Regresa pronto!')
            salir = True
        else:
            print('Opcion invalida, selecciona otra opcion...\n')

def comprar_producto(snacks, productos):
    id_snack = int(input('Que snack quieres (id)?: '))
    #productos.append(snacks[id_snack])
    #print(f'Ok. snack agregado: {snacks[id_snack]}')

    # Recorrer la lista de snacks
    snack_encontrado = None
    for snack in snacks.lista_snacks:
        if id_snack == snack.id:
            snack_encontrado = snack
            break

    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Ok, snack agregado: {snack_encontrado}')
    else:
        print(f'El id del snack es incorrecto: {id_snack}')

def mostrar_ticket(productos):
    ticket = f'\t*** Ticket de Venta ***'
    total = 0
    for producto in productos:
        ticket += f"\n\t- {producto.nombre} - ${producto.precio}"
        total += producto.precio
    ticket += f'\n\tTOTAL -> ${total}'
    print(ticket)

def agregar_snack(snacks):
    nombre = input('Dame el nombre del snack: ')
    precio = int(input('Dame el precio del snack: '))
    nuevo_snack = Snack(nombre, precio)
    snacks.agregar_snack(nuevo_snack)
    print(f'Tu snack {nuevo_snack} se ha agregado correctamente!')
    print(snacks)

# Llamamos o invocamos la funcion maquina snacks
maquina_snacks(snacks, productos)