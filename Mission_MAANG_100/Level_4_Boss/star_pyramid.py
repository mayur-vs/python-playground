user_input_number = int(input("Enter a number - how many times pyramid you want? "))

for i in range(1, user_input_number + 1) :
    pattern = "*" * i
    print(pattern)