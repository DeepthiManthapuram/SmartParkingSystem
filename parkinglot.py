from parkingspot import ParkingSpot
from vehicle import Vehicle


class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        print(f"--- Parking Lot: {self.name} ---")
        for spot in self.spots:
            status = "Occupied" if spot.is_occupied() else "Free"
            print(f"Spot {spot.spot_id} ({spot.get_size()}): {status}")

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot.is_occupied() and spot.assign_vehicle(vehicle):
                return True
        print("No suitable spot found!")
        return False

    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot.is_occupied():
                removed = spot.remove_vehicle()
                if removed and removed.get_license_plate() == vehicle.get_license_plate():
                    fee = vehicle.calculate_parking_fee(hours)
                    print(f"Parking fee for {vehicle.get_license_plate()} = ₹{fee}")
                    return fee
        print("Vehicle not found in parking lot.")
        return 0


