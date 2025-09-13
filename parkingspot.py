from vehicle import Bike, Car, SUV, Truck

class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.__size = size        # private attribute
        self.__is_occupied = False
        self.__vehicle = None

    def get_size(self):
        return self.__size

    def is_occupied(self):
        return self.__is_occupied

    def assign_vehicle(self, vehicle):
        if self.__is_occupied:
            print(f"Spot {self.spot_id} already occupied!")
            return False

        # Vehicle type restriction
        if isinstance(vehicle, Bike) and self.__size in ["S", "M", "L", "XL"]:
            pass
        elif isinstance(vehicle, Car) and self.__size in ["M", "L", "XL"]:
            pass
        elif isinstance(vehicle, SUV) and self.__size in ["L", "XL"]:
            pass
        elif isinstance(vehicle, Truck) and self.__size == "XL":
            pass
        else:
            print(f"Vehicle {vehicle.get_license_plate()} does not fit in spot {self.spot_id} ({self.__size})")
            return False

        self.__vehicle = vehicle
        self.__is_occupied = True
        print(f"Vehicle {vehicle.get_license_plate()} parked at spot {self.spot_id}")
        return True
    
        
    def remove_vehicle(self):
        if not self.__is_occupied:
            print(f"Spot {self.spot_id} is already empty.")
            return None
        vehicle = self.__vehicle
        self.__vehicle = None
        self.__is_occupied = False
        print(f"Vehicle {vehicle.get_license_plate()} removed from spot {self.spot_id}")
        return vehicle