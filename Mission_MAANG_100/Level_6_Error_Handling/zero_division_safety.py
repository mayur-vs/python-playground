try :  
    user_input_first_number = int(input("Enter a first number: "))
    user_input_second_number = int(input("Enter a second number: "))
    result = user_input_first_number / user_input_second_number
    print(f"Here is the {user_input_first_number} divided by {user_input_second_number} : {result:.2f}")
except ZeroDivisionError :
    print("You cannot divide by zero!, please enter a number which is greater than 0")