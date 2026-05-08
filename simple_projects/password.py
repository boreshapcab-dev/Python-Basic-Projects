def password_checker():
    
    password = ["boresh" , "mahesh"]

    word = input("Enter the word: ")
    
           
    if word in password:
            print("Log in successfully")

    else:
            print("Enter the correct password")



def letter_check(string , answer):
    found = False 
    word = "boresh"
    
    for letter in word:    
        
        if letter == answer:
            found = True
            break

    if found:
        print("Letter present")

    else:
        print("Not present")
             
        
letter_check("boresh" , 'r')


        