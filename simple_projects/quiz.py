def get_count(choice):
    if choice == 1:
        return True
    elif choice == 0:
        return False
    

def question():
    answers = ["Tiger"]

    question1 = "Which is the national anomal of india"
    print(question1)
    result = input("Enter the answer: ")

    for answer in answers:
        if answer == result:
           correct_answer = get_count()

        choice = input("Enter your choice: ")
   

question()
