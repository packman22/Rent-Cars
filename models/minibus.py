from .vehicle import Vehicle

class Minibus(Vehicle):
    def calculate_rental_price(self):
        return super().calculate_rental_price() + 2
