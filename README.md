# What I Learned in This Course

In this course, I learned the fundamental concepts of Object-Oriented Programming (OOP). Here's a summary of what I learned:

## Key Concepts

- **Object-Oriented Programming (OOP)**
  - A programming paradigm that uses objects to design and build applications.

- **Encapsulation**
  - Grouping data (attributes) and methods (functions) that operate on that data into a single unit (class).
  - Example: A `Vehicle` class that has attributes like `brand`, `model`, `price`, and methods like `sell`, `check_available`.

- **Abstraction**
  - Hiding complex implementation details and showing only the necessary functionality.
  - Example: Abstract methods like `start_engine` and `stop_engine` in the `Vehicle` class that must be implemented by subclasses.

- **Inheritance**
  - Creating new classes based on existing classes, inheriting their attributes and methods.
  - Example: `Car`, `Bike`, and `Truck` classes inheriting from the `Vehicle` class.

- **Polymorphism**
  - Allowing methods to do different things based on the object it is acting upon.
  - Example: The `start_engine` method behaves differently in the `Car`, `Bike`, and `Truck` classes.

## Practical Application

- **Defining Classes**
  - Learned how to create classes with attributes and methods.

- **Creating Objects**
  - Learned how to create instances of classes (objects) and use them.

- **Using Inheritance**
  - Learned how to create subclasses that inherit from a superclass and override methods.

- **Implementing Polymorphism**
  - Learned how to define methods in subclasses that behave differently even though they have the same name.

## Code Example

Here's a simple code example that demonstrates these concepts:

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
