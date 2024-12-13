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
p1=Person("sara")
p1.introduce()
s1=Student("ammar",24)
s1.more_info()
s1.introduce()

