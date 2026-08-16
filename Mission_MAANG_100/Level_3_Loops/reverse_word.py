user_input_text = input("Enter a word: ")

for index in range(len(user_input_text)) :
    print(user_input_text[len(user_input_text) - index - 1])