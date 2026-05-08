
def check_balance():
    balance = 1000
    print("your account balance is " , balance)

def deposiste_amount():
    balance = 1000
    amount = int(input("Enter the amount to be deposited "))

    if(amount > 0):
        
        print("Amount deposited")

    else:
        print("Enter the valid amount")

    balance = balance + amount
    print("your current balance is " , balance)

def withdraw_amount():
    balance = 1000
    amount = int(input("Enter the withdeawal amount"))

    if(amount <= balance and amount > 0):
        balance = balance - amount
        print("Your current balance is " , balance)

    else:
        print("insufficient balance")

while True:
    print("1. check balance")
    print("2. deposite amount")
    print("3. withdraw amount")
    print("4. exit")

    choice = int(input("Enter the choice"))


    if(choice == 1):
        check_balance()

    elif(choice == 2):
        deposiste_amount()

    elif(choice == 3):
        withdraw_amount()

    elif(choice == 4):
        print("Thank you for visiting")

    else:
        print("invalid choice")

