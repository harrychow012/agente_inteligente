import tkinter as tk
from interfaz.controlador_ventana import VentanaPrincipal


def main():
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()