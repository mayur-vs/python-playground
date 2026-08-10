user_input_year = int(input("Enter a year: "))

if (user_input_year % 4 == 0 and user_input_year % 100 != 0) or (user_input_year % 400 == 0) :
    print(f"{user_input_year} is a leap year.")
else :
    print(f"{user_input_year} is not a leap year.")