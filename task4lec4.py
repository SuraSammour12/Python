# Task 4 solution :dictionary

# Define a dictionary
student={'name':'sura','age':22,'course':'python'}
print(f"student dictionary before update :{student}")

# Update function
student.update({'age':23,'phone_number':2212})
print(f"student dictionary after update :{student}")

# Delete course key
del student['course']
#or 
#student.pop('course')
print(f"student dictionary after delete course key :{student}")