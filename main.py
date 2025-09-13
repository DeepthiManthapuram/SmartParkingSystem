
from vehicle import Bike, Car, SUV, Truck
from parkingspot import ParkingSpot
from parkinglot import ParkingLot
from payment import CashPayment, CardPayment, UPIPayment

if __name__ == "__main__":
    # Create Parking Lot
    lot = ParkingLot("Downtown Parking")
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "L"))
    lot.add_spot(ParkingSpot(4, "XL"))

    # Create Vehicles
    bike = Bike("B123", "Alice")
    car = Car("C456", "Bob", 4)
    suv = SUV("S789", "Charlie")
    truck = Truck("T999", "David", 20000)

    # Park Vehicles
    lot.park_vehicle(bike)
    lot.park_vehicle(car)
    lot.park_vehicle(suv)
    lot.park_vehicle(truck)

    lot.show_spots()

    # Unpark and Payment
    fee = lot.unpark_vehicle(car, 2)  # 2 hours
    if fee > 0:
        payment_method = UPIPayment()   # Can switch to CashPayment() or CardPayment()
        payment_method.process_payment(fee)

    lot.show_spots()
