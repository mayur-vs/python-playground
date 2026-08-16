user_input_number = input("Enter a number: ")

user_input_number_length = len(user_input_number)
sum_of_power_of_digits = 0

for each_char in user_input_number :
    sum_of_power_of_digits = sum_of_power_of_digits + (int(each_char) ** user_input_number_length)

if str(sum_of_power_of_digits) == user_input_number :
    print(f"Number is a Armstrong Number")
else :
    print(f"Number is not a Armstrong Number")