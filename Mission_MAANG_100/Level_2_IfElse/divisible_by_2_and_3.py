user_input_number = int(input('Enter the number: '))

# Least Common Multiple of 2 and 3 is 6, so we can check directly with 6
# if number is dividing 6 then it is obviously go to divide 2 and 3
if user_input_number % 6 == 0 :
    print(f"{user_input_number} is divisible by 2 and 3")
else :
    print(f"{user_input_number} is not divisible by 2 and 3")