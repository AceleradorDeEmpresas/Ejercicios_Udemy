import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        # Configuramos el grid
        self.configurar_grid()
        #mostrar tabla
        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry("600x400")
        self.resizable(0, 0)
        self.configure(background="#1d2d44")
        self.title("Manejo de tabla con POO")

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

    def mostrar_tabla(self):
        # Estilo de la tabla
        estilo = ttk.Style()
        estilo.theme_use("clam") # Estilo de la tabla
        estilo.configure("Treeview", background="black",
                        foreground="white", 
                        fieldbackground="black",
                        rowheight=25)
        estilo.map("Treeview", background=[("selected", "#1d2d44")]) # Color de la tabla al seleccionar una fila

        # Definimos las columnas
        columnas = ("Id", "Nombre", "Edad")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings")

        #Cabeceras 
        self.tabla.heading("Id", text="Id", anchor=tk.CENTER)
        self.tabla.heading("Nombre", text="Nombre", anchor=tk.W)
        self.tabla.heading("Edad", text="Edad", anchor=tk.W)

        # Formato 
        self.tabla.column("Id", width=80, anchor=tk.CENTER)
        self.tabla.column("Nombre", width=120, anchor=tk.W)
        self.tabla.column("Edad", width=120, anchor=tk.W)

        # Cargar datos a la tabla 
        datos = ((1, "Alex", 37), (2, 'Monica', 32))
        for persona in datos: 
            self.tabla.insert(parent="", index=tk.END, values=persona)

        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)


        # Añadir scrollbar
        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Añadimos el evento al hacer click en la tabla
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_seleccionado)

    # Añadir un evento al hacer click en la tabla
    def mostrar_seleccionado(self, event):
        # Obtenemos el item seleccionado 
        item = self.tabla.selection()[0]
        # Obtenemos los valores del item seleccionado 
        valores = self.tabla.item(item, "values")
        print(valores)
        # Mostramos los valores en una ventana emergente
        messagebox.showinfo("Seleccionado", f"ID: {valores[0]}\nNombre: {valores[1]}\nEdad: {valores[2]}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
