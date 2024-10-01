# Week 4 - Part 1: Basic OOP Concepts

# 1. Define a basic class for Vehicles
class Vehicle:
    """Vehicle class - Base class for all vehicles"""

    def __init__(self, make, model, year):
        """Constructor to initialize vehicle attributes"""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Method to display vehicle information"""
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

# 2. Creating subclasses using Inheritance
class Car(Vehicle):
    """Car class - Inherits from Vehicle"""

    def __init__(self, make, model, year, doors):
        """Constructor to initialize car-specific attributes"""
        super().__init__(make, model, year)  # Call the constructor of Vehicle
        self.doors = doors

    def display_info(self):
        """Override display_info to include number of doors"""
        super().display_info()  # Call the parent class's display_info method
        print(f"Doors: {self.doors}")

class Bike(Vehicle):
    """Bike class - Inherits from Vehicle"""

    def __init__(self, make, model, year, type_of_bike):
        """Constructor to initialize bike-specific attributes"""
        super().__init__(make, model, year)  # Call the constructor of Vehicle
        self.type_of_bike = type_of_bike

    def display_info(self):
        """Override display_info to include type of bike"""
        super().display_info()  # Call the parent class's display_info method
        print(f"Type of Bike: {self.type_of_bike}")

# 3. Polymorphism Example
class Dog:
    """Dog class with a sound method"""
    def sound(self):
        return "Bark"

class Cat:
    """Cat class with a sound method"""
    def sound(self):
        return "Meow"

# 4. Encapsulation and Abstraction
class BankAccount:
    """BankAccount class with private attributes and public methods"""
    
    def __init__(self, account_number, balance):
        """Constructor to initialize private attributes"""
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        """Method to deposit money"""
        self.__balance += amount

    def withdraw(self, amount):
        """Method to withdraw money with balance check"""
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        """Public method to access the private balance"""
        return self.__balance

# Week 5 - Part 2: Building a Mini Inventory System

# Inventory System using OOP principles
class InventoryItem:
    """Base class for items in an inventory"""

    def __init__(self, name, price, quantity):
        """Constructor to initialize item attributes"""
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_item(self):
        """Method to display item details"""
        print(f"Item: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

class CarInventory(InventoryItem, Car):
    """CarInventory class that extends both InventoryItem and Car"""
    
    def __init__(self, name, price, quantity, make, model, year, doors):
        """Constructor to initialize car-specific inventory attributes"""
        InventoryItem.__init__(self, name, price, quantity)  # Initialize InventoryItem attributes
        Car.__init__(self, make, model, year, doors)  # Initialize Car attributes

    def display_item(self):
        """Override method to display car-specific details"""
        super().display_item()  # Display InventoryItem details
        Car.display_info(self)  # Display Car details

class BikeInventory(InventoryItem, Bike):
    """BikeInventory class that extends both InventoryItem and Bike"""
    
    def __init__(self, name, price, quantity, make, model, year, type_of_bike):
        """Constructor to initialize bike-specific inventory attributes"""
        InventoryItem.__init__(self, name, price, quantity)  # Initialize InventoryItem attributes
        Bike.__init__(self, make, model, year, type_of_bike)  # Initialize Bike attributes

    def display_item(self):
        """Override method to display bike-specific details"""
        super().display_item()  # Display InventoryItem details
        Bike.display_info(self)  # Display Bike details

# Week 5 - Example to show Polymorphism in action
def make_sound(animal):
    """Function to demonstrate polymorphism by calling sound method"""
    print(animal.sound())

# Main function to run the examples
if __name__ == "__main__":
    # 1. Basic Class Usage
    vehicle = Vehicle("Toyota", "Camry", 2022)
    vehicle.display_info()  # Display basic vehicle info

    # 2. Inheritance: Car and Bike
    car = Car("Honda", "Civic", 2020, 4)
    car.display_info()

    bike = Bike("Yamaha", "R1", 2021, "Sport")
    bike.display_info()

    # 3. Polymorphism: Dog and Cat sounds
    dog = Dog()
    cat = Cat()
    make_sound(dog)  # Output: Bark
    make_sound(cat)  # Output: Meow

    # 4. Encapsulation: BankAccount with private attributes
    account = BankAccount("12345678", 1000)
    account.deposit(500)
    print("Balance after deposit:", account.get_balance())  # Output: 1500
    account.withdraw(200)
    print("Balance after withdrawal:", account.get_balance())  # Output: 1300

    # 5. Inventory System
    car_item = CarInventory("Sedan", 25000, 5, "Toyota", "Camry", 2022, 4)
    bike_item = BikeInventory("Motorbike", 15000, 3, "Yamaha", "R1", 2021, "Sport")

    print("\nInventory System:")
    car_item.display_item()  # Display car inventory
    bike_item.display_item()  # Display bike inventory
