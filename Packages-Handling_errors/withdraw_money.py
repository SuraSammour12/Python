# Real Example:
def withdraw_money(balance,amount):
    try:
        if amount>balance:
            print("Insufficient funds")
            return #Exit the function if there's not enough balance
        else:
            balance-=amount
            print(f"withdrawal successful. Your new balance is : {balance}")
    except:
        print("enter a valid number")
    finally:
        print("Transaction complete...logging transaction")
balance=7000
withdraw_money(balance,1000)