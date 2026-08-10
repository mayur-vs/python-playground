user_first_number = int(input("Enter the first number: "))
user_second_number = int(input("Enter the second number: "))
user_third_number = int(input("Enter the third number: "))

if user_first_number > user_second_number and user_first_number > user_third_number:
    print(f"{user_first_number} is the greatest among the three numbers.")
elif user_second_number > user_third_number:
    print(f"{user_second_number} is the greatest among the three numbers.")
else:
    if user_first_number == user_second_number and user_first_number == user_third_number:
        print(f"All three numbers are equal.")
    else:
        print(f"{user_third_number} is the greatest among the three numbers.")