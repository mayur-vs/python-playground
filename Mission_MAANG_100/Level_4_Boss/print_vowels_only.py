user_input_word = input("Enter a word: ")

for each_char in user_input_word :
    if each_char.lower() in "aeiou" :
        print(each_char)