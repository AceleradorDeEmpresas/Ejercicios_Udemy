import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="personas_db"
)

cursor = personas_db.cursor()
# Se crea la sentencia en los valores se deben de tener Placeholders
sentencia = "INSERT INTO persona(nombre, apellido, edad) VALUES (%s, %s, %s)"
# Se crea la tupla con los valores que se añadirán en los placeholders de la sentencia
valores = ("Carolina", "Ramos", 20)
# Se ejecuta la sentencia SQL con los valores de la tupla
cursor.execute(sentencia, valores)
personas_db.commit() # Guarda los cambios en la base de datos
# Cerramos la conexión
personas_db.close()