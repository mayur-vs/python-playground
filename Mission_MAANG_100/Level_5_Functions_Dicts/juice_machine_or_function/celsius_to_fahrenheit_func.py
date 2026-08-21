def celsius_to_fahrenheit(celsius) :
    return (celsius * 9/5) + 32

user_input_celsius = float(input("Enter a temperature in Celsius: "))
temperature_in_fahrenheit = celsius_to_fahrenheit(user_input_celsius)
print(f"Temperature in fahrenheit : {temperature_in_fahrenheit:.2f}")