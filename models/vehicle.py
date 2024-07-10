class Vehicle:
    def __init__(self, license_plate, rental_days):
        self._license_plate = license_plate
        self._rental_days = rental_days

    def calculate_rental_price(self):
        base_price = 50 * self._rental_days
        return base_price
