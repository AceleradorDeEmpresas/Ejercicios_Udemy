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

def saludar(nombre):
    mensaje = f"Saludos... {nombre}"
    print(mensaje)
    # Muestra un mensaje en una ventana emergente
    showinfo(title="Mensaje", message=mensaje)

# Botones 
boton1 = ttk.Button(ventana, text="Enviar", command=lambda: saludar("alex"))

boton1.pack(pady=20)

# Este metodo va al final para que se aga visible la ventana
# Hacemos visible la ventana 
ventana.mainloop()