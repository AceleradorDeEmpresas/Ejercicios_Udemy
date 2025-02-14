import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login Application')
ventana.configure(background='#1d2d44')

# Creamos un estilo 
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground="white",
                  fieldbackground='black')



ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)


# Agregamos un frame 
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(0, weight=3)

# titulo 
etiqueta = ttk.Label(frame, text="Login", font=('Arial', 20))
etiqueta.grid(row=0, column=0, columnspan=2)

usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1, column="1", sticky=tk.E, padx=5, pady=5)

# Usuario 
etiqueta_usuario = ttk.Label(frame, text="Usuario: ", font=('Arial', 16))
etiqueta_usuario.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

# Password
etiqueta_password = ttk.Label(frame, text="Password: ")
etiqueta_password.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_caja_texto = ttk.Entry(frame, show="*")
password_caja_texto.grid(row=2, column="1", sticky=tk.E, padx=5, pady=5)

# Botón
login_boton = ttk.Button(frame, text="Enviar")
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

frame.grid(row=0, column=0)


def validar(evento):
    usuario = usuario_caja_texto.get()
    password = password_caja_texto.get()
    # Usuario = root, password = admin
    if usuario == 'root' and password == 'admin':
        showinfo(title='login', message='Usuario correcto')
    else:
        showerror(title='login', message='Usuario o contraseña incorrectos')
# Asociar los eventos al botón de login 
login_boton.bind('<Return>', validar) # Presionar la tecla de enter
login_boton.bind('<Button-1>', validar) # Clic izquierdo del mouse


ventana.mainloop()