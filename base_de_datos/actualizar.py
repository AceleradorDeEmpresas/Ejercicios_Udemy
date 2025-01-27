import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="personas_db"
)

cursor = personas_db.cursor()
# Se crea la sentencia en los valores se deben de tener Placeholders
sentencia = "UPDATE persona SET nombre=%s, apellido=%s WHERE id=%s"
# Se crea la tupla con los valores que se añadirán en los placeholders de la sentencia
valores = ("Amanda", "Lopez", 5)
cursor.execute(sentencia, valores)
personas_db.commit() # Guarda los cambios en la base de datos, sólo se usa cuando modificamos la base de datos con INSERT, UPDATE y DELETE
# Cerramos la conexión
personas_db.close()
