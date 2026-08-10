user_input_temperature = int(input("Enter the temperature in Celsius: "))

if user_input_temperature > 30:
    print("Hot")
elif user_input_temperature > 15 and user_input_temperature <= 30:
    print("Warm")
else:
    print("Cold")