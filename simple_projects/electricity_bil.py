def electricity_bil_generator():

    #electricity_bill = 101

    units = int(input("Enter the number of units: "))

    if(units <= 100):
        print("Your electricity bill is free")

    elif(units <= 200):
        electricity_bill = (units - 100) * 2

        print("your electricity bill is " , electricity_bill)

    elif(units >= 300):
        electricity_bill = (units - 100) * 5
        print("your electricity bill is " , electricity_bill)

    
    

electricity_bil_generator()


