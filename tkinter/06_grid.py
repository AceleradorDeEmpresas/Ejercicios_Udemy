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

# Configurar el grid
#Columnas
# Con el método columnconfigure podemos asignar un tamaño a las columnas en un grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
# Renglones 
# Con el método rowconfigure podemos asignar un tamaño a las columnas en un renglon
ventana.rowconfigure(0, weight=1)


# Manejo de grid de manera horizontal
boton1 = ttk.Button(ventana, text="Botón 1")
boton2 = ttk.Button(ventana, text="Botón 2")
boton3 = ttk.Button(ventana, text="Botón 3")

# Publicar usando grid 
# Para poder alinear elementos dentro de un renglon o columna,
# debemos usar la propiedad sticky, seguida de las constantes 
# Norte: tk.N, tk.NE, tk.NO
# Este: tk.E
# Sur: tk.S, tk.SE
# Oeste: tk.W, tk.SW, tk.SW
boton1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N)
# Aplicaremos un padding interno al botón con las propiedades
# ipadx e ipady 
boton2.grid(row=0, column=1, ipadx=16, ipady=10)
# Para que un elemento crezca de a lo alto y ancho de una columna o renglon
# usamos las propiedades de sticky: tk.NS para el alto y tk.NSEW para que abarque todo el ancho
boton3.grid(row=0, column=2, padx=10, pady=10, sticky=tk.NSEW)


# Este metodo va al final para que se aga visible la ventana
# Hacemos visible la ventana 
ventana.mainloop()