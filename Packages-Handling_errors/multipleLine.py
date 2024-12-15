# writing multiple lines with writelines
lines = ["First line\n", "Second line\n", "Third line\n"]
with open ('output.txt','w') as file:
        file.writelines(lines)
