from .vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, license_plate, rental_days, pma):
        super().__init__(license_plate, rental_days)
        self.pma = pma

    def calculate_rental_price(self):
        return super().calculate_rental_price() + 20 * self.pma
