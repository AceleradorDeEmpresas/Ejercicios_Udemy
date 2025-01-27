import tkinter as tk
from tkinter import ttk # Mejora del paquete de Tkinter

# creamos una ventana
ventana = tk.Tk()

# Redimensionar la ventana 
ventana.geometry("600x400")

# Evitar redimensionar la ventana 
ventana.resizable(0,0)

# Color de la ventana 
ventana.configure(background="#1d2d44")

# Titulo de nuesta ventana 
ventana.title("Evitar redimensionar")


#Crea un etiqueta (label)
etiqueta = tk.Label(ventana, text="Saludos hol.a mundo desde TKinter..")

# Cambiar el texto usando configure
etiqueta.configure(text="Nos vemos...")

# Cambiar valor de la etiqueta por medio de la llave text 
etiqueta['text'] = "Adios..."

#Mostramos el componente de etiqueta 
etiqueta.pack(pady=50)

# Este metodo va al final para que se aga visible la ventana
# Hacemos visible la ventana 
ventana.mainloop()