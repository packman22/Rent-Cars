from .van import Van

class Truck(Van):
    def calculate_rental_price(self):
        return super().calculate_rental_price() + 40
