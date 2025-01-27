# Clase

class Contacto:
    def inicializar_contacto(self, nombre, apellido, celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email

    # Métodos
    def mostrar_contacto(self):
        print(f'''
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Celular: {self.celular}
            Email: {self.email}
                ''')
            
        
            
# Código principal
print("*** Clases y objetos en Python ***")
#Crear un primer objeto
contacto_1 = Contacto()
contacto_1.inicializar_contacto("Monica", "Campos", "6182279242", "moniendo@gmail.com")
contacto_1.mostrar_contacto()
print(f"Direccion de memoria: {id( contacto_1 )}")

# Crear un segundo objeto 
contacto_2 = Contacto()
contacto_2.inicializar_contacto("Willy", "NataplumitaCano", "618890823", "natawillyflores@gmail.com")
contacto_2.mostrar_contacto()