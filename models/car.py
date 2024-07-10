from .vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, license_plate, rental_days):
        super().__init__(license_plate, rental_days)

    def calculate_rental_price(self):
        base_price = super().calculate_rental_price()
        return base_price + 1.5 * self._rental_days
