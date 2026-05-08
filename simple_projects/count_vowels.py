def count_vowels():
    word = input("Enter the word: ")
    count = 0
    for char in word:
        if (char == 'a' or
            char == 'e' or
            char == 'i' or
            char == 'o' or
            char == 'u' or
            char == 'A' or
            char == 'E' or
            char == 'I' or
            char == 'O' or
            char == 'U' ):

            counter = counter + 1

    return counter
    
#input = "apple"
#print(f"the number of vowels in the {input} is {count_vowels}")
    
