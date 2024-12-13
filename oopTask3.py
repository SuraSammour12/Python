# OOP Task 3 solution

# Create a Person class with a constructor "superclass"
class Person:
    def __init__(self,name):
        self.name=name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")
# Create a Student class "subclass" with a constructor
class Student(Person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    
    def more_info(self):
        print(f"Student {self.name} is {self.age} years old.")
# Test 
P1=Person("sara")
P1.introduce()
S1=Student("ammar",24)
S1.more_info()
S1.introduce()

