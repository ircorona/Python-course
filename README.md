# What I Learned in This Course

In this course, I learned about Object-Oriented Programming (OOP). Here’s a simple breakdown of what I discovered:

## Key Concepts

- **Object-Oriented Programming (OOP)**
  - A way to design and build computer programs using "objects" that represent real-world things.

- **Encapsulation**
  - Combining data (like a car’s brand, model, and price) and actions (like selling a car) into one unit called a class.
  - Example: The `Vehicle` class groups together the car’s brand, model, and price with actions like `sell` and `check_available`.

- **Abstraction**
  - Hiding the complex details and only showing the important stuff.
  - Example: The `start_engine` method in the `Vehicle` class doesn’t have a specific action but says that each type of vehicle (like cars or trucks) should have this method.

- **Inheritance**
  - Creating new classes from existing ones. New classes get the same features and methods as the original class but can also add or change things.
  - Example: The `Car`, `Bike`, and `Truck` classes get their basic features from the `Vehicle` class but have their own specific details.

- **Polymorphism**
  - Allowing different classes to use the same method name but perform different actions.
  - Example: The `start_engine` method does different things for `Car`, `Bike`, and `Truck`.

## Practical Application

- **Defining Classes**
  - Learned how to create classes with data and actions.

- **Creating Objects**
  - Learned how to make instances of classes (like creating a specific car or bike).

- **Using Inheritance**
  - Learned how to make new classes based on existing ones.

- **Implementing Polymorphism**
  - Learned how to make methods that work differently depending on the object.

## Code Example

Here’s a simple code example showing these concepts:

```python
class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"The vehicle {self.brand} has been sold.")
        else:
            print(f"The vehicle {self.brand} is not available.")

    def check_available(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("This method must be implemented by the subclass")

    def stop_engine(self):
        raise NotImplementedError("This method must be implemented by the subclass")

class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The engine of the car {self.brand} is running."
        else:
            return f"The car {self.brand} is not available."

    def stop_engine(self):
        if not self.is_available:
            return f"The engine of the car {self.brand} has stopped."
        else:
            return f"The car {self.brand} is not available."

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Sorry, {vehicle.brand} is not available.")

    def inquire_vehicle(self, vehicle):
        if vehicle.check_available():
            availability = "Available"
        else:
            availability = "Not available"
        print(f"The {vehicle.brand} is {availability} and costs {vehicle.get_price()}.")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle):
        self.inventory.append(vehicle)
        print(f"The {vehicle.brand} has been added to the inventory.")

    def register_customers(self, customer):
        self.customers.append(customer)
        print(f"The customer {customer.name} has been added.")

    def show_available_vehicle(self):
        print("Vehicles available in the store:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f" - {vehicle.brand} for {vehicle.get_price()}.")

# Create vehicle objects (instances)
car1 = Car("Toyota", "Corolla", "20000")
customer1 = Customer("Carlos")
dealer = Dealership()

# Add vehicles to the dealership's inventory
dealer.add_vehicles(car1)

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
