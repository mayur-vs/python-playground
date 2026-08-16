user_input_string = input("Enter a text: ")

if user_input_string.lower() == user_input_string[::-1].lower() :
    print(f"{user_input_string} is a palindrome")
else :
    print(f"{user_input_string} is not a palindrome")