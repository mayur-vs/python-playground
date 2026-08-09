principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))

simple_interest = (principal_amount * rate_of_interest * time_period) / 100

print(f"The simple interest is: {simple_interest:.2f}")