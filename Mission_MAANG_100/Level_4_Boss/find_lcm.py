# Least Common Multiple
user_input_number_one = int(input("Enter a number one: "))
user_input_number_two = int(input("Enter a number two: "))

if user_input_number_one > user_input_number_two :
    maximum_number = user_input_number_one
else :
    maximum_number = user_input_number_two

greater = maximum_number
while True :
    if greater % user_input_number_one == 0 and greater % user_input_number_two == 0 :
        lcm_result = greater
        break
    else :
        greater += 1

print(f"Lowest Common Multiple : {greater}")