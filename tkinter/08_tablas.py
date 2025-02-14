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

ventana.columnconfigure(0, weight=1)

# Definimos las columnas
columnas = ("Id", "Nombre", "Edad")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

#Cabeceras 
tabla.heading("Id", text="Id", anchor=tk.CENTER)
tabla.heading("Nombre", text="Nombre", anchor=tk.W)
tabla.heading("Edad", text="Edad", anchor=tk.W)

# Formato 
tabla.column("Id", width=80)
tabla.column("Nombre", width=120)
tabla.column("Edad", width=120)

# Cargar datos a la tabla 
datos = ((1, "Alex", 37), (2, 'Monica', 32))
for persona in datos: 
    tabla.insert(parent="", index=tk.END, values=persona)

tabla.grid(row=0, column=0, sticky=tk.NSEW)


# Este metodo va al final para que se aga visible la ventana
# Hacemos visible la ventana 
ventana.mainloop()