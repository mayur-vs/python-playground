user_input_number = int(input("Enter a number: "))

factorial_of_number = 1

for number in range(user_input_number, 0, -1) :
    factorial_of_number *= number

print(f"Factorial of {user_input_number} is {factorial_of_number}") 