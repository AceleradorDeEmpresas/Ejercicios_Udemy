import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Tk):
    COLOR_VENTANA = "#1D2D44"


    def __init__(self):
        super().__init__()
        self.configurar_ventana()

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
# 
#       
if __name__ == "__main__":
    app = App()
    app.mainloop()
