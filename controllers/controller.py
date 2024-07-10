from models.car import Car
from models.minibus import Minibus
from models.van import Van
from models.truck import Truck

class RentalController:
    def calculate_price(self, vehicle_type, license_plate, rental_days, pma=0):
        if vehicle_type == "Car":
            vehicle = Car(license_plate, rental_days)
        elif vehicle_type == "Minibus":
            vehicle = Minibus(license_plate, rental_days)
        elif vehicle_type == "Van":
            vehicle = Van(license_plate, rental_days, pma)
        elif vehicle_type == "Truck":
            vehicle = Truck(license_plate, rental_days, pma)
        else:
            raise ValueError("Tipo de vehículo desconocido")
        
        return vehicle.calculate_rental_price()
