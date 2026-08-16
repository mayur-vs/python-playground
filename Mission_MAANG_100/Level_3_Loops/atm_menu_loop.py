counter = True
while counter :
    print("Enter any one of this option: Check Balance, Withdraw, Exit")
    user_input_text = input("")

    if user_input_text.lower() == "exit" :
        counter = False