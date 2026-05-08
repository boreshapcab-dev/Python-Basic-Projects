def addition():
    number1 = int(input("Enter the number1: "))
    number2 = int(input("Enter the number2: "))

    sum = number1 + number2
    print("The sum is" , sum)

def substraction():
    number1 = int(input("Enter the number1: "))
    number2 = int(input("Enter the number2: "))

    difference = number1 - number2
    print("The difference  is " , difference)

def multiplication():
    number1 = int(input("Enter the number1: "))
    number2 = int(input("Enter the number2: "))

    product = number1 * number2
    print("The product is" , product)

while True:
    print("1. addition")
    print("2. substraction")
    print("3. multiplication")

    choice = int(input("Enter the choice"))
    if(choice == 1):
        addition()

    elif(choice == 2):
        substraction()

    elif(choice == 3):
        multiplication()

    else:
        print("Invalid choice")
