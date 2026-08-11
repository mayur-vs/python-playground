user_input_number = int(input('Enter the number: '))

if (user_input_number % 2 == 0) and (user_input_number % 3 == 0) :
    print(f"{user_input_number} is divisible by 2 and 3")
else :
    print(f"{user_input_number} is not divisible by 2 and 3")