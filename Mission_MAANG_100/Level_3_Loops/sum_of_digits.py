user_input_number = input("Enter a number: ")

sum_of_digits = 0

for each_char_number in user_input_number :
    sum_of_digits += int(each_char_number)

print(f"sum of digits is {sum_of_digits}")