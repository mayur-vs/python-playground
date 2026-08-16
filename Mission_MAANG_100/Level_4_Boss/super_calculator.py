while True :
    user_input = input("Press 1 for Add, 2 for Subtract, 3 for Multiply, 4 for Divide, or type 'Quit' to exit : ")
    
    if not user_input.isdigit() and user_input.lower() == "quit" :
        break

    user_input_number_one = int(input("Enter a number one: "))
    user_input_number_two = int(input("Enter a number two: "))
    
    match int(user_input) :
        case 1 :
            operation_result = user_input_number_one + user_input_number_two
            print(f"Addition of {user_input_number_one} + {user_input_number_two}: {operation_result}")

        case 2 :
            operation_result = user_input_number_one - user_input_number_two
            print(f"Substraction of {user_input_number_one} - {user_input_number_two}: {operation_result}")

        case 3 :
            operation_result = user_input_number_one * user_input_number_two
            print(f"Multiplication of {user_input_number_one} * {user_input_number_two}: {operation_result}")

        case 4 :
            if user_input_number_two <= 0 :
                print("Cannot be divied by 0")
            else :
                operation_result = user_input_number_one / user_input_number_two
                print(f"Division of {user_input_number_one} / {user_input_number_two}: {operation_result}")    
        case _ :
            print("Enter a Invalid operation!")