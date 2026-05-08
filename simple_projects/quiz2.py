def quiz_app():
    score = 0
    print("1. which is the capital city of india?")
    print("a) Bangalore  b)Delhi  c)Mumbai")

    ans = input("Enter answer: ")

    if ans == "b":
        print("Right answer")

    else:
        print("Wrong answer")


    print("1. what is the sum of 2 + 2?")
    print("a) 3  b)1  c)4")

    ans = input("Enter answer: ").lower()

    if ans == "c":
        print("Right answer")

    else:
        print("Wrong answer") 

    score = score + 1
    

quiz_app()