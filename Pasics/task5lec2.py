# Task 5 solution : Condition
number=int(input("Enter number : "))
if number % 2 == 0 and number % 5 == 0 :
    print("Number is divisible by 5 and 2")

elif number % 2 == 0 :
    print("Number is divisible by 2")
    
elif number % 5 == 0 :
    print("Number is divisible by 5")

else:
    print("Number is not divisible by 5 or 2")