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
ventana.title("Evitar redimensionar")

def mostrar():
    texto = caja_texto.get() # Recuperando el valor de la caja de texto
    print(f"Texto proporcionado: {texto}")
    # Accedemos al texto de etiqueta 
    etiqueta["text"] = texto
# Caja de texto
caja_texto = ttk.Entry(ventana, font=("arial", 15))
caja_texto.pack(pady=25)

# Botón que de enviar 
boton = ttk.Button(ventana, text="Enviar..", command=mostrar)
boton.pack(pady=30)

# Agregar etiqueta 
etiqueta = ttk.Label(ventana, text="Valor inicial")
etiqueta.pack(pady=20)

# Este metodo va al final para que se aga visible la ventana
# Hacemos visible la ventana 
ventana.mainloop()