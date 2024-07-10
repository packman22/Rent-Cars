import tkinter as tk
from tkinter import ttk, messagebox

class RentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Rental Pricing")
        self.create_widgets()

    def create_widgets(self):
        # Aquí se definirán los widgets de la interfaz gráfica

        # Ejemplo:
        label = ttk.Label(self.root, text="Bienvenido a la aplicación de alquiler de vehículos")
        label.pack()

        # Añadir más widgets según sea necesario

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = RentalApp(root)
    app.run()
