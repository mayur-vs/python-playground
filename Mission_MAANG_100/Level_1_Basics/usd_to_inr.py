dollar_amount = float(input("Enter amount in USD: "))

exchange_rate = 83.0 #  # Example exchange rate, you can update it as needed

inr_amount = dollar_amount * exchange_rate

print(f"{dollar_amount:.2f} USD is equal to {inr_amount:.2f} INR.")