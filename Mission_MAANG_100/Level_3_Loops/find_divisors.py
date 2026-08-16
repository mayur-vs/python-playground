user_input_number = int(input("Enter a number: "))

divisor_string = ""

for divisor in range(1, user_input_number + 1) :
    if user_input_number % divisor == 0 :
        divisor_string += str(divisor) + ","

print(divisor_string.rstrip(","))