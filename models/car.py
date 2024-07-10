from .vehicle import Vehicle

class Car(Vehicle):
    def calculate_rental_price(self):
        return super().calculate_rental_price() + 1.5 * self.rental_days
