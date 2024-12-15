# Classroom task solution :
# Method 1: 
capital_letters=[]
for i in range(65,91):
    capital_letters.append(chr(i))
print(capital_letters)

print("\n")

# Method 2:
capital_letters2=[]
start_point=ord('A')
end_point=ord('Z')
for j in range(start_point,end_point+1):
    capital_letters2.append(chr(j))
print(capital_letters2)

