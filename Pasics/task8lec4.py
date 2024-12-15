# Task 8 solution : function

def num_type(lst:list):
    for i in lst:
        if i %2==0:
            print(f"{i} : Even",end=" | ")
        elif i%2!=0:
             print(f"{i} : Odd",end=" |")

num_type([6,8,5,2,9,1])
  