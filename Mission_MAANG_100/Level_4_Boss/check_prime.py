user_input_number = int(input("Enter a number: "))

if user_input_number <= 1 :
    print(f"{user_input_number} is not a prime number")
else :
    divisible_counter = 0
    for each_number_between in range(2, user_input_number) :
        if user_input_number % each_number_between == 0 :
            divisible_counter += 1
            break

    if divisible_counter == 0 :
        print(f"{user_input_number} number is a prime number")
    else :
        print(f"{user_input_number} is not a prime number")