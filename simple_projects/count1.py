
def count_vowels(string):
    counter = 0
    
    if string != None:
     for character in string:
        if (character == 'a' or
            character == 'e' or
            character == 'i' or
            character == 'o' or
            character == 'u' or
            character == 'A' or
            character == 'E' or
            character == 'I' or
            character == 'O' or
            character == 'U'  ):

            counter = counter + 1
    
    else:
        print("Enter the string only")

    return counter
      
input = "apple"
print(f"Number of vowels in the {input} is = {count_vowels(input)}")