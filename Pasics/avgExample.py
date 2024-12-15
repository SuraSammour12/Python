def print_avg():
    total=0
    count=0
    while True:
        mark=input("Enter a mark :").upper()
        if mark=='Q':
            break
        try:
            mark=float(mark)
            total+=mark
            count+=1
        except ValueError:
            print("Wrong")
        
    if count==0:
        print("NO Mark")
    else:
        avg=total/count
        print(f"Average is : {avg}")

print_avg()