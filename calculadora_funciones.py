print("*** Calculadora con Funciones *** ")
def mostrar_menu():
    opciones = [
        "1. Sumar",
        "2. Restar",
        "3. Multiplicar",
        "4. Dividir",
        "5. Salir"
    ]

    for opcion in opciones:
        print(f"{opcion}")

def pedir_valores():
    val_1 = float(input("Ingresa el primer valor: "))
    val_2 = float(input("Ingresa el segundo valor: "))

    return (val_1, val_2)

def ejecutar_operacion(opcion, salir):
    opcion = int(input("Seleccione la operación: "))
    if opcion == 1:
        print("*** Haz seleccionado la función de sumar ***")
        val_1, val_2 = pedir_valores()
        resultado = val_1 + val_2
        print(f"Total: {resultado}")
    elif opcion == 2:
        print("*** Haz seleccionado la función de restar ***")
        val_1, val_2 = pedir_valores()
        resultado = val_1 - val_2
        print(f"Total: {resultado}")
    elif opcion == 3:
        print("*** Haz seleccionado la función de multiplicar ***")
        val_1, val_2 = pedir_valores()
        resultado = val_1 * val_2
        print(f"Total: {resultado}")
    elif opcion == 4:
        print("*** Haz seleccionado la función de divid ***")
        val_1, val_2 = pedir_valores()
        resultado = val_1 / val_2
        print(f"Total: {resultado}")
    elif opcion == 5:
        salir = True
        print("Saliendo de la aplicación")
        return salir
    else:
        print("Opción inválida")

# Código principal
salir = False
while not salir: 
    opcion = mostrar_menu()
    salir = ejecutar_operacion(opcion, salir)


