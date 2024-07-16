from .vehicle import Vehicle

class Minibus(Vehicle):
    def calculate_rental_price(self):
            base_price = super().calculate_rental_price()
            return base_price + 1.5 * self._rental_days + 2
