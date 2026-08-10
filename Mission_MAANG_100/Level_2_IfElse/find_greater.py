user_first_number = int(input("Enter the first number: "))
user_second_number = int(input("Enter the second number: "))

if user_first_number > user_second_number:
    print(f"{user_first_number} is greater than {user_second_number}.")
elif user_first_number < user_second_number:
    print(f"{user_first_number} is less than {user_second_number}.")
else:
    print(f"{user_first_number} is equal to {user_second_number}.")