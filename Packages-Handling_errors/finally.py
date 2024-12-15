# finally
try:
    number=int(input("Enter a number :"))
    result=100/number
except:
    print("Something went wrong")
else:
    print(f"The result is : {result}")
finally:
    print("This block will always execute")