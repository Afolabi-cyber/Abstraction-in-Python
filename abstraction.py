from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def move(self):
        pass  # Abstract method without implementation

# Concrete class 1
class Car(Vehicle):
    def move(self):
        return "The car drives on the road."

# Concrete class 2
class Airplane(Vehicle):
    def move(self):
        return "The airplane flies in the sky."

# Concrete class 3
class Boat(Vehicle):
    def move(self):
        return "The boat sails on water."

# Client code
vehicles = [Car(), Airplane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
