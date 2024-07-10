import tkinter as tk
from views.gui import RentalApp

if __name__ == "__main__":
    root = tk.Tk()
    app = RentalApp(root)
    app.run()
