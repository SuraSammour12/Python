# Task 1 solution

list1=[1,2,3,4]
list2=[1,4,5,6]

for i in list1:
    for j in list2:
        if i == j:
            print(i)
        else:
            print("Not in special numbers.")