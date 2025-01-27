# Listas con Diccionarios 
print("*** Listas y diccionarios ***")

personas = [
    {
        'nombre': 'Regina',
        'apellido': 'Flores',
        'edad': 21
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 35
    },
    {
        'nombre': 'Monica',
        'apellido': 'Campos',
        'edad': 31
    }
]


# Imprimir la primer persona 
# print(personas[0])

# Acceder a un valor (llave) del primer elemento
# print(personas[0].get('nombre'))

# Recorrer los elementos de la lista (elemento = diccionario) 
for contador , persona in enumerate(personas):
    print(f'{contador} - {persona.get("nombre")}')
