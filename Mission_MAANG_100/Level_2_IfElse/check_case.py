user_input_character = input("Enter your character: ")

if user_input_character.isalpha() :
    if (user_input_character.lower() == user_input_character) :
        print(f"Your entered {user_input_character} character is lowercase")
    elif user_input_character.isalpha() and (user_input_character.upper() == user_input_character) :
        print(f"Your entered {user_input_character} character is uppercase")
else :
    print('Please enter a valid alphabet between A to Z or a to z')