user_input_number = int(input("Enter a number: "))

sum_of_numbers = 0

for number in range(1, user_input_number + 1) :
    sum_of_numbers += number

print(sum_of_numbers)