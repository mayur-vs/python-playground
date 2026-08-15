user_input_number = input("Enter a number between 0 to 10: ")


if user_input_number.isdigit() :
    if 0 <= int(user_input_number) <= 10 :
        secret_number = 7
        if int(user_input_number) == secret_number :
            print("You have guessed the right number!, you won the match")
        else :
            print("You haven't guessed the right number, please try again!")
    else :
        print("Please enter a number between 0 to 10, please try again!")
else :
    print("Invalid input, please enter a number between 0 to 10")