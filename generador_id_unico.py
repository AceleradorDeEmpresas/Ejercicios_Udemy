# Generador de ID Único

from random import randint


print("*** Sistema de Generador ID único  ***")
nombre = input("Cual es tu nombre?: ")
nombre_2 = nombre[0:2].upper()
print(nombre_2)

apellido = input("Cual es tu apellido?: ")
apellido_2 = apellido[0:2].upper()
print(apellido_2)

fecha_nacimiento = input("Igresa tu fecha de nacimiento: ")

fecha_nacimiento_2 = fecha_nacimiento[2:3]

# Generar un valor de cuatro digitos de manera aleatoria
generar_id = randint(0,9999)

id_unico = f'{nombre_2}{apellido_2}{fecha_nacimiento_2}{generar_id}'

print(f"""
    Hola {nombre}, habitante de ciudad gotica!
    Tu nuevo número de identificación (ID) generado por el sistema es:
    {id_unico}
    Recuerda que este ID es único y seguro para ti. 
    ¡Felicidades!
""")

