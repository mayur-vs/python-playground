user_input_temperature = int(input("Enter the temperature in Celsius: "))

if user_input_temperature > 30:
    print("Hot")
elif 15 < user_input_temperature <= 30:
    print("Warm")
else:
    print("Cold")