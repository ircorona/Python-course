# Define a class (Encapsulation)
# Encapsulation: Grouping data (attributes) and methods that operate on that data within a single unit, the class.
# Abstraction: Hiding implementation details and showing only the necessary functionality.
class Vehicle:
    def __init__(self, brand, model, price):
        # Encapsulation: Private attributes of the Vehicle class.
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
    
    def sell(self):
        # Encapsulation: Method that operates on the encapsulated attributes.
        if self.is_available:
            self.is_available = False
            print(f"The vehicle {self.brand} has been sold.")
        else:
            print(f"The vehicle {self.brand} is not available.")

    def check_available(self):
        # Encapsulation: Method that returns the availability status of the vehicle.
        return self.is_available
    
    def get_price(self):
        # Encapsulation: Method that returns the price of the vehicle.
        return self.price
    
    def start_engine(self):
        # Abstraction: Abstract method that must be implemented by subclasses.
        raise NotImplementedError("This method must be implemented by the subclass")
    
    def stop_engine(self):
        # Abstraction: Abstract method that must be implemented by subclasses.
        raise NotImplementedError("This method must be implemented by the subclass")

# Inheritance: The Car class inherits from the Vehicle class.
class Car(Vehicle):
    # Polymorphism: Specific implementation of the abstract start_engine method for the Car class.
    def start_engine(self):
        if not self.is_available:
            return f"The engine of the car {self.brand} is running."
        else:
            return f"The car {self.brand} is not available."
        
    # Polymorphism: Specific implementation of the abstract stop_engine method for the Car class.
    def stop_engine(self):
        if not self.is_available:
            return f"The engine of the car {self.brand} has stopped."
        else:
            return f"The car {self.brand} is not available."

# Inheritance: The Bike class inherits from the Vehicle class.
class Bike(Vehicle):
    # Polymorphism: Specific implementation of the abstract start_engine method for the Bike class.
    def start_engine(self):
        if not self.is_available:
            return f"The bike {self.brand} is running."
        else:
            return f"The bike {self.brand} is not available."
        
    # Polymorphism: Specific implementation of the abstract stop_engine method for the Bike class.
    def stop_engine(self):
        if not self.is_available:
            return f"The bike {self.brand} has stopped."
        else:
            return f"The bike {self.brand} is not available."

# Inheritance: The Truck class inherits from the Vehicle class.
class Truck(Vehicle):
    # Polymorphism: Specific implementation of the abstract start_engine method for the Truck class.
    def start_engine(self):
        if not self.is_available:
            return f"The engine of the truck {self.brand} is running."
        else:
            return f"The truck {self.brand} is not available."
        
    # Polymorphism: Specific implementation of the abstract stop_engine method for the Truck class.
    def stop_engine(self):
        if not self.is_available:
            return f"The engine of the truck {self.brand} has stopped."
        else:
            return f"The truck {self.brand} is not available."

# Define the Customer class
# Encapsulation: Grouping data (attributes) and methods that operate on that data within a single unit, the class.
class Customer:
    def __init__(self, name):
        # Encapsulation: Private attributes of the Customer class.
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        # Encapsulation: Method that operates on the encapsulated attributes.
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Sorry, {vehicle.brand} is not available.")

    def inquire_vehicle(self, vehicle: Vehicle):
        # Encapsulation: Method that operates on the encapsulated attributes.
        if vehicle.check_available():
            availability = "Available"
        else:
            availability = "Not available"
        print(f"The {vehicle.brand} is {availability} and costs {vehicle.get_price()}.")

# Define the Dealership class
# Encapsulation: Grouping data (attributes) and methods that operate on that data within a single unit, the class.
class Dealership:
    def __init__(self):
        # Encapsulation: Private attributes of the Dealership class.
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        # Encapsulation: Method that operates on the encapsulated attributes.
        self.inventory.append(vehicle)
        print(f"The {vehicle.brand} has been added to the inventory.")

    def register_customers(self, customer: Customer):
        # Encapsulation: Method that operates on the encapsulated attributes.
        self.customers.append(customer)
        print(f"The customer {customer.name} has been added.")

    def show_available_vehicle(self):
        # Encapsulation: Method that operates on the encapsulated attributes.
        print("Vehicles available in the store:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f" - {vehicle.brand} for {vehicle.get_price()}.")

# Create vehicle objects (instances)
car1 = Car("Toyota", "Corolla", "20000")
car2 = Car("Honda", "Civic", "22000")
car3 = Car("Ford", "Mustang", "35000")
bike1 = Bike("Yamaha", "YZF-R1", "15000")
truck1 = Truck("Volvo", "FH16", "50000")

# Create a customer object (instance)
customer1 = Customer("Carlos")

# Create a dealership object (instance)
dealer = Dealership()

# Add vehicles to the dealership's inventory
dealer.add_vehicles(car1)
dealer.add_vehicles(car2)
dealer.add_vehicles(car3)
dealer.add_vehicles(bike1)
dealer.add_vehicles(truck1)

# Register the customer with the dealership
dealer.register_customers(customer1)

# Show available vehicles
dealer.show_available_vehicle()

# Customer inquires about a vehicle
customer1.inquire_vehicle(car1)

# Customer buys a vehicle
customer1.buy_vehicle(car1)

# Show available vehicles again
dealer.show_available_vehicle()

# Customer tries to buy the same vehicle again
customer1.buy_vehicle(car1)
