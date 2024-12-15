# Handling Specific Errors
try:
        number=int(input("Enter a number:"))
        print(f"100 divided by {number} is: {100/number}")
except ValueError:
        print("Invalid input. Please enter a number.")

except ZeroDivisionError:
        print("Oops! U Can't divide by zero.")
   
