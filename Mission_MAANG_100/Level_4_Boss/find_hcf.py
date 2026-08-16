# Highest Common Factor
user_input_number_one = int(input("Enter a first number: "))
user_input_number_two = int(input("Enter a second number: "))

if user_input_number_one > user_input_number_two :
    minimum_number = user_input_number_two
else :
    minimum_number = user_input_number_one

for each_factor in range(minimum_number, 0, -1) :
    if user_input_number_one % each_factor == 0 and user_input_number_two % each_factor == 0 :
        hcf_result = each_factor
        break

print(f"Highest common factor: {hcf_result}")