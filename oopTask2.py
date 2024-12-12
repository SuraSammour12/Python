# OOP Task 2 solution

# Creat Truck Class
class Truck:
    def __init__(self,name,color,year):
        self.name=name
        self.color=color
        self.year=year
# start engine method
    def start_engine(self):
        print(f"The {self.name}-{self.color} is starting {self.year}")

# Create an instance of Truck Class
my_truck=Truck("KAMAZ","brown",2024)
my_truck.start_engine()