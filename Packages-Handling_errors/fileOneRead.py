# Open the file for reading ('r' mode)
file=open('example.txt','r')
content=file.read()

print(f"content of the file : {content}")
file.close()