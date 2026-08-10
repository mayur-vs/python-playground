user_input_character = input("Enter a character: ")

if user_input_character in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    print(f"{user_input_character} is a vowel.")
else :
    print(f"{user_input_character} is a consonant.")