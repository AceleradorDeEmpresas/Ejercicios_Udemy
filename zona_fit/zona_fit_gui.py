import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror, showinfo
from cliente import Cliente
from cliente_dao import Cliente_Dao

class App(tk.Tk):
    COLOR_VENTANA = "#1D2D44"


    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry("900x600")
        self.title("Zona Fit")
        self.resizable(0, 0)
        self.configure(background=App.COLOR_VENTANA)
        # Aplicamos el estilo a la ventana
        self.estilos = ttk.Style()
        self.estilos.theme_use("clam")
        self.estilos.configure(self,
                                background=App.COLOR_VENTANA,
                                foreground="white",
                                font=("Arial", 12),
                                fieldbackground="black")

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
    
    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text="Zona Fit (GYM)", font=("Arial", 30),
                             background=App.COLOR_VENTANA,
                             foreground="white")
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_f = ttk.Frame()
        #Nombre
        nombre_l = ttk.Label(self.frame_f, text='Nombre:', padding=10) 
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30)
        self.nombre_t = ttk.Entry(self.frame_f)
        self.nombre_t.grid(row=0, column=1)
        self.frame_f.grid(row=1, column=0)
        #Apellido
        apellido_l = ttk.Label(self.frame_f, text='Apellido:', padding=10) 
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30)
        self.apellido_t = ttk.Entry(self.frame_f)
        self.apellido_t.grid(row=1, column=1)
        #Membresia
        membresia_l = ttk.Label(self.frame_f, text='Membresia:', padding=10) 
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30)
        self.membresia_t = ttk.Entry(self.frame_f)
        self.membresia_t.grid(row=2, column=1)

    #Boton agregar
    def mostrar_botones(self):
        self.frame_b = ttk.Frame()
        # Creamos los botones
        # Boton agregar
        agregar_b = ttk.Button(self.frame_b,
                               text="Agregar",
                               command=self.validar_cliente)
        agregar_b.grid(row=0, column=0, padx=30)
        eliminar_b = ttk.Button(self.frame_b,
                                text="Eliminar",
                                command=self.eliminar_cliente)
        eliminar_b.grid(row=0, column=1, padx=30)

        limpiar_b = ttk.Button(self.frame_b,
                               text="Limpiar",
                               command=self.limpiar_datos)
        limpiar_b.grid(row=0, column=3, padx=30)

        # Aplicando estilos a los botones
        self.estilos.configure("TButton",
                               background="#005f53",
                               foreground="white",
                               font=("Arial", 12),
                               padding=10)
        self.estilos.map("TButton",
                         background=[("active", "black")],
                         foreground=[("active", "white")])

        # Publicando el frame
        self.frame_b.grid(row=2, column=0, columnspan=2, padx=30, pady=40)

    def validar_cliente(self):
        #Validamos cada uno de los campos
        if (self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.agregar_cliente()
            else:
                showerror(title='Atención', message='El valor de membresía no es númerico')
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus_set()
        else:
            showerror(title='Atención', message='Todos los campos son obligatorios')
            self.nombre_t.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
        except ValueError as e:
            return False
    def agregar_cliente(self):
        # Recuperar los valores de las cajas de texto
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
        Cliente_Dao.insertar(cliente)
        showinfo(title='Agregar', message='Cliente agregado correctamente...')
        # Volemos a mostrar los datos
        self.recarga_datos()
    
    def recarga_datos(self):
        self.cargar_tabla()
        # limpiamos datos
        self.limpiar_datos()
    
    

    def limpiar_datos(self):
        self.limpiar_formulario()
    
    def limpiar_formulario(self):
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)

    # Método para mostrar la tabla
    def cargar_tabla(self):
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla 
        self.estilos.configure("Treeview", 
        background='black',
        foreground='white',
        fieldbackground='black',
        rowheight=30)
        columnas = ('ID', 'Nombre', 'Apellido', 'Membresia')
        #Creamos la tabla 
        self.tabla = ttk.Treeview(self.frame_tabla,
                                  columns=columnas,
                                  show='headings',
                                  height=10) 
        #Agregamos los cabeceros
        self.tabla.heading('ID', text='ID', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresia', anchor=tk.W)
        #Definimos las columnas 
        self.tabla.column('ID', anchor=tk.CENTER, width=80)
        self.tabla.column('Nombre', anchor=tk.W, width=120)
        self.tabla.column('Apellido', anchor=tk.W, width=120)
        self.tabla.column('Membresia', anchor=tk.W, width=120)

        # Cargar los datos de la BD
        clientes = Cliente_Dao.seleccionar()
        for c in clientes:
            self.tabla.insert(parent='',
                              index=tk.END,
                              values=(c.id, c.nombre, c.apellido, c.membresia))
            
        # Agregamos la barra de desplazamiento
        self.scrollbar = ttk.Scrollbar(self.frame_tabla, 
                                         orient=tk.VERTICAL,
                                         command=self.tabla.yview)
        
        self.tabla.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

        #Mostramos la tabla 
        self.tabla.grid(row=0, column=0)
        # Mostramos el frame
        self.frame_tabla.grid(row=1, column=1,  padx=30)          

    def eliminar_cliente(self):
        pass

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
