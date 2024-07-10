class Vehicle:
    def __init__(self, license_plate, rental_days):
        self.license_plate = license_plate
        self.rental_days = rental_days

    def calculate_rental_price(self):
        return 50 * self.rental_days
