def student_grade():
    
    total_marks = 600

    kannada =int( input("Enter the marks of kannada"))
    english =int( input("Enter the marks of english"))
    physics = int(input("Enter the marks for physics"))
    chemistry = int(input("Enter the marks for chemistry"))
    biology =int( input("Enter the marks for biology"))
    maths = int(input("Enter the marks for maths"))


    total = kannada + english + physics + chemistry + biology + maths
    print("Total marks = " , total)

    percentage = (total / total_marks) * 100
    print("Total percentage  = " , percentage)

    if(percentage > 90):
            print("Distinction")

    elif(percentage < 70):
            print("First class")

    elif(percentage < 60):
            print("second class")

    elif (percentage < 30):
            print("failed")

    


student_grade()
