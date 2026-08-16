sum_of_numbers = 0
while True :
    user_input_number = int(input("Enter a number: "))
    if user_input_number == 0 or user_input_number == -0 :
        break
    sum_of_numbers += user_input_number

print(f"Sum of Number until zero: {sum_of_numbers}")