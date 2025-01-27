import tkinter 

# creamos una ventana
ventana = tkinter.Tk()

# Redimensionar la ventana 
ventana.geometry("600x400")

# Evitar redimensionar la ventana 
ventana.resizable(0,0)

# Color de la ventana 
ventana.configure(background="#1d2d44")

# Titulo de nuesta ventana 
ventana.title("Evitar redimensionar")

# Hacemos visible la ventana 
ventana.mainloop()