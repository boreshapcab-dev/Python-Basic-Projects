def get_seat_price(choice):

    if choice == 1:
        return 150, "Normal"
    elif choice == 2:
        return 250, "Premium"
    
def movie_ticket_booking():
    print("Welcome to movie ticket booking")

    print("1. Normal seat - 150")
    print("2. Premium - 250")

    choice = int(input("Enter your choice: "))
    tickets = int(input("Enter number of tickets: "))

    price , seat_type = get_seat_price(choice)

    if(seat_type == "invalid"):
        print("Invalid seat selection")

    total = price * tickets

    print("Booking details")
    print("Seat_type:" , seat_type)
    print("Tickets:" , tickets)
    print("Total amount:" , total)
        
movie_ticket_booking()