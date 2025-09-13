#Base Vehicle Class
class Vehicle:
    def __init__(self,license_plate,owner_name):
        self.__license_plate = license_plate    #private attribute
        self.__owner_name = owner_name          #private attribute

    # Getter and Setter for license_plate
    def get_license_plate(self):
        return self.__license_plate
    
    def set_license_plate(self,plate):
        self.__license_plate = plate

    # Getter and Setter for owner_name
    def get_owner_name(self):
        return self.__owner_name
    
    def set_owner_name(self,name):
        self.__owner_name = name

    #methods to override
    def display(self):
        raise NotImplementedError("Subclass must override display method")
    
    def calculate_parking_fee(self):
        raise NotImplementedError("Subclass must override calculate_parking_fee method")

# Derived classes
class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"[Bike] Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Helmet: {self.helmet_required}")
    
    def calculate_parking_fee(self, hours):
        return 20 * hours
    
class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"[Car] Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Seats: {self.seats}")

    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"[SUV] Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, 4WD: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity=10000):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"[Truck] Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Capacity: {self.max_load_capacity}kg")

    def calculate_parking_fee(self, hours):
        return 100 * hours