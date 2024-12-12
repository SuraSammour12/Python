# OOP Task 1 solution
"""A class representing a truck with a model and color"""
class Truck:
    def __init__(self,model,color):
        self.model=model
        self.color=color

model=input("Enter your model :")    
color=input("Enter your color :")
# Create an instance of the truck class
my_truck=Truck(model,color)

# Print its model and color
print(f"Truck model : {my_truck.model}")
print(f"Truck color : {my_truck.color}")

