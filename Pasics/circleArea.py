# Lecture 4 Functions:Function to calculate the area of a circle.
import math
def calculate_circle_area():
    try:
         radius=float(input("Enter Circle Radius:"))
         if radius<0:
              print("Circle radius must be positive !")
         else:
            area=math.pi*radius**2
            print(f"Area is = {area:.2f}")
    except ValueError:
         print("Invalid input. Please enter a numeric value.")
calculate_circle_area()