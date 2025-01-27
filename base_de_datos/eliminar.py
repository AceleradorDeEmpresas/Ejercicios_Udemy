import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="personas_db"
)


cursor = personas_db.cursor()
sentencia = "DELETE FROM persona WHERE id=%s"
valores = (5,) # Para convertir este valor a tupla, hay que agregar una coma; ","
cursor.execute(sentencia, valores)
personas_db.commit()
personas_db.close()