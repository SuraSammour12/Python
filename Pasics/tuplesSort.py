# Lecture 4 Functions:
# Write a function that takes a list of tuples and sorts them based on the second element of each tuple

def sort_tuples(tuples):

# Sort the list based on the second element of each tuple
    return sorted(tuples,key=lambda x:x[1])

# Test the function
test_tuples=[("a",3),("b",1),("c",2)]
sorted_tuples=sort_tuples(test_tuples)
print("sorted_tuples :",sorted_tuples)