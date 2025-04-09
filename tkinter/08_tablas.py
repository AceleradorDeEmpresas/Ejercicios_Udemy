import tkinter as tk
from tkinter import ttk # Mejora del paquete de Tkinter
from tkinter.messagebox import showinfo # importamos una ventana emergente para mostrar mensajes o alertas

# creamos una ventana
ventana = tk.Tk()

# Redimensionar la ventana 
ventana.geometry("600x400")

# Evitar redimensionar la ventana 
ventana.resizable(0,0)

# Color de la ventana 
ventana.configure(background="#1d2d44")

# Titulo de nuesta ventana 
ventana.title("Manejo de tabla")

# Configuremos el grid
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(1, weight=0)


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
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

#Cabeceras 
tabla.heading("Id", text="Id", anchor=tk.CENTER)
tabla.heading("Nombre", text="Nombre", anchor=tk.W)
tabla.heading("Edad", text="Edad", anchor=tk.W)

# Formato 
tabla.column("Id", width=80, anchor=tk.CENTER)
tabla.column("Nombre", width=120, anchor=tk.W)
tabla.column("Edad", width=120, anchor=tk.W)

# Cargar datos a la tabla 
datos = ((1, "Alex", 37), (2, 'Monica', 32))
# datos = ((1, "Alex", 37), (2, 'Monica', 32)) + ((1, "Alex", 37), (2, 'Monica', 32)) +((1, "Alex", 37), (2, 'Monica', 32)) + ((1, "Alex", 37), (2, 'Monica', 32)) + ((1, "Alex", 37), (2, 'Monica', 32)) + ((1, "Alex", 37), (2, 'Monica', 32)) + ((1, "Alex", 37), (2, 'Monica', 32)) + ((1, "Alex", 37), (2, 'Monica', 32)) + ((1, "Alex", 37), (2, 'Monica', 32)) + ((1, "Alex", 37), (2, 'Monica', 32))
for persona in datos: 
    tabla.insert(parent="", index=tk.END, values=persona)

tabla.grid(row=0, column=0, sticky=tk.NSEW)


# Añadir scrollbar
scrollbar = tk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

# Añadir un evento al hacer click en la tabla
def mostrar_seleccionado(event):
    # Obtenemos el item seleccionado 
    item = tabla.selection()[0]
    # Obtenemos los valores del item seleccionado 
    valores = tabla.item(item, "values")
    print(valores)
    # Mostramos los valores en una ventana emergente
    showinfo("Seleccionado", f"ID: {valores[0]}\nNombre: {valores[1]}\nEdad: {valores[2]}")

# Añadimos el evento al hacer click en la tabla
tabla.bind('<<TreeviewSelect>>', mostrar_seleccionado)

# Este metodo va al final para que se aga visible la ventana
# Hacemos visible la ventana 
ventana.mainloop()