import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="personas_db"
)

mi_cursor = personas_db.cursor()
mi_cursor.execute("SELECT id, nombre, apellido FROM persona")
resultado = mi_cursor.fetchall()
for persona in resultado:
    print(persona)


personas_db.close() # Cerramos la conexión con la BD