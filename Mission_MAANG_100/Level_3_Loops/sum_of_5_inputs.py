sum_of_numbers = 0
numbers_text = ""

for i in range(5) :
    user_input_number = int(input("Enter a number: "))
    numbers_text = numbers_text + str(user_input_number)
    numbers_text += ", "
    sum_of_numbers += user_input_number


print(f"Sum of your {numbers_text.rstrip(', ')} numbers are {sum_of_numbers}")