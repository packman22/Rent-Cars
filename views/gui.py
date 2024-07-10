import tkinter as tk
from tkinter import ttk, messagebox
from controllers.controller import RentalController

class RentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Rental Pricing")
        self.controller = RentalController()
        self.create_widgets()

    def create_widgets(self):
        # Menú de selección de tipo de vehículo
        self.vehicle_type_var = tk.StringVar()
        ttk.Label(self.root, text="Tipo de vehículo:").grid(column=0, row=0, padx=10, pady=10)
        self.vehicle_type_combo = ttk.Combobox(self.root, textvariable=self.vehicle_type_var)
        self.vehicle_type_combo['values'] = ("Car", "Minibus", "Van", "Truck")
        self.vehicle_type_combo.grid(column=1, row=0, padx=10, pady=10)

        # Campo de entrada para la matrícula
        self.license_plate_var = tk.StringVar()
        ttk.Label(self.root, text="Matrícula:").grid(column=0, row=1, padx=10, pady=10)
        self.license_plate_entry = ttk.Entry(self.root, textvariable=self.license_plate_var)
        self.license_plate_entry.grid(column=1, row=1, padx=10, pady=10)

        # Campo de entrada para los días de alquiler
        self.rental_days_var = tk.IntVar()
        ttk.Label(self.root, text="Días de alquiler:").grid(column=0, row=2, padx=10, pady=10)
        self.rental_days_entry = ttk.Entry(self.root, textvariable=self.rental_days_var)
        self.rental_days_entry.grid(column=1, row=2, padx=10, pady=10)

        # Campo de entrada para el PMA (solo para vehículos de carga)
        self.pma_var = tk.IntVar()
        ttk.Label(self.root, text="PMA (toneladas):").grid(column=0, row=3, padx=10, pady=10)
        self.pma_entry = ttk.Entry(self.root, textvariable=self.pma_var)
        self.pma_entry.grid(column=1, row=3, padx=10, pady=10)

        # Botón para calcular el precio
        self.calculate_button = ttk.Button(self.root, text="Calcular Precio", command=self.calculate_price)
        self.calculate_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

        # Etiqueta para mostrar el resultado
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

    def calculate_price(self):
        vehicle_type = self.vehicle_type_var.get()
        license_plate = self.license_plate_var.get()
        rental_days = self.rental_days_var.get()
        pma = self.pma_var.get()

        try:
            price = self.controller.calculate_price(vehicle_type, license_plate, rental_days, pma)
            self.result_label.config(text=f"Precio de alquiler: {price} COP")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = RentalApp(root)
    app.run()
