from conexion import Conexion
from cliente import Cliente
class Cliente_Dao: 
    # Querys
    SELECCIONAR = "SELECT * FROM persona"
    INSERTAR = "INSERT INTO persona (nombre, apellido, membresia) VALUES (%s, %s, %s)"
    ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM persona WHERE id=%s"

    @classmethod 
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente 
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Ocurrió un error al seleccionar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_pool(conexion)

    @classmethod 
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount #Nos indica cuántos datos se insertaron en la BD
        except Exception as e:
            print(f"Ocurrion un error al insertar el cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_pool(conexion)

    @classmethod 
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount #Nos indica cuántos datos se actualizaron en la BD
        except Exception as e:
            print(f"Ocurrio un error al insertar el cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_pool(conexion)
    
    @classmethod
    def eliminar(cls, cliente):
        conexion = None 
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount #Nos indica cuántos datos se eliminaron en la BD
        except Exception as e:
            print(f"Ocurrión un error al intentar eliinar al cliente: {e}") 
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_pool(conexion)

if __name__ == "__main__":
    #Insertar Cliente
    # cliente1 = Cliente(nombre="Willt", apellido="Flores", membresia=500)
    # clientes_insertados = Cliente_Dao.insertar(cliente1)
    # print(f"Clientes Insertados: {clientes_insertados}")
    # Actualización 
    # cliente_actualizar = Cliente(5, "Alexa", "Tellez", 400)
    # clientes_actualizados = Cliente_Dao.actualizar(cliente_actualizar)
    # print(f"Clientes Actualizados: {cliente_actualizar}")
    #Eliminar Cliente 
    # cliente_eliminar = Cliente(id=5)
    # clientes_eliminados = Cliente_Dao.eliminar(cliente_eliminar)
    # print(f"Clientes Eliminados: {clientes_eliminados}")
    # Seleccionar clientes 
    clientes = Cliente_Dao.seleccionar()
    for cliente in clientes:
        print(cliente)