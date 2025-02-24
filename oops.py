# Dependency: One class depends on another when it uses it as a parameter or local variable.
class Printer:
    def print_document(self, document):
        print(f"Printing document: {document}")

class User:
    def __init__(self, name):
        self.name = name

    def use_printer(self, printer, document):
        print(f"{self.name} is using the printer.")
        printer.print_document(document)

# Generalization: Demonstrates inheritance where the superclass generalizes behavior.
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Specialization: Subclass provides more specific behavior.
class SportsCar:
    def drive(self):
        print("Driving fast!")

class ElectricSportsCar(SportsCar):  # Specialization
    def charge_battery(self):
        print("Charging the battery.")


from abc import ABC, abstractmethod
# Inheritance: Shape is an abstract class, and Rectangle inherits from it.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


# Aggregation: Engine class can exist independently, and is used in the Car class.
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print(f"Engine with {self.horsepower} HP started.")

class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start_car(self):
        print("Starting the car.")
        self.engine.start()

#Assocaition: Both is independent and no one owns the other
class teacher:
    def __init__(self,name):
        this.name = name

# Testing the classes
# Dependency (->)
printer = Printer()
user = User("Alice")
user.use_printer(printer, "My Report")

#Generalization
dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow

#Specialization
sports_car = SportsCar()
sports_car.drive()  # Output: Driving fast!

#Realization
electric_car = ElectricSportsCar()
electric_car.drive()  # Output: Driving fast!
electric_car.charge_battery()  # Output: Charging the battery.

#Aggregation
engine = Engine(200)
car = Car(engine)
car.start_car()

rectangle = Rectangle(5, 10)
print(f"Area of rectangle: {rectangle.area()}")




