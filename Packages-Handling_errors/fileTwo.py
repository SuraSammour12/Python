# Method 2 to create and write on a file
with open('example2.txt','w') as file:
    for x in range(10):
        file.write('Hi file-2\n')