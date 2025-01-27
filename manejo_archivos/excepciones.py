# El manejo de excepciones ocurre cuando hay un error en nuestro programa y podemmos procesarlo con try - except 

# try -> Bloque de código que revisa si hay errores a procesar 
# except -> es el blque que proesa el error en caso de que haya habido alguno
print("*** Manejo de excepciones ***")
try: 
    # print(mi_variable)
    # 10/0
    x = int(input("Dame el valor de X: "))
    if x == 0:
        # Con la paralabra Rise podemos personalizar excepciones dentro de nuestro programa
        raise Exception("Error la variable x es 0")
except Exception as e:
    print(f"Ocurrio un error: {e}") 
# Este bloque de código se ejecutará sólo cuando no haya errores.
else: 
    print("El valor de la variable x es distinto de 0 ")
# Este bloque de código se ejecutará sin importar si har errores o no 
finally: 
    print(f"Valor de x validado: {x}")
