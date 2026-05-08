def odd_even():

    number = int(input("Enter the number: "))
    if number % 2 == 0:
        print("Even number")

    else:
        print("Odd number")

def print_square():
    number = int(input("Enter the number: "))

    square = number * number
    print("The square of two numbers is: " , square)

def print_cube():
    number = int(input("Enter the number: "))

    cube = number * number * number
    print("The cube of two numbers is: " , cube)

print("__menu__")
print("1. odd_even")
print("2. print_square")
print("3. print_cube")

choice = int(input("Enter your choice: "))

if(choice == 1):
    odd_even()
elif(choice == 2):
    print_square()
elif(choice == 3):
    print_cube()

else:
    print("invalid choice")

