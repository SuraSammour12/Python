# This is Abstaction Example code
from abc import ABC,abstractmethod

class Car(ABC):
     @abstractmethod
     def start_engine(self):
        pass
     def fill_fuel(self):
        print("filling fuel...")

class car1(Car):
    def start_engine(self):
        print("car engine start")

# my_car1=Car().start_engine() => TypeError: Can't instantiate abstract class Car without an implementation for abstract method 'start_engine'
my_car=car1()
my_car.start_engine()
my_car.fill_fuel()
