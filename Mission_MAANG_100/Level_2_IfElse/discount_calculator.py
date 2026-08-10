user_bill_amount = float(input("Enter the bill amount: "))

if user_bill_amount > 1000:
    discount = user_bill_amount * 0.10
    final_bill_amount =  user_bill_amount - discount
    print(f"Your final bill amount is {final_bill_amount:.2f} after giving 10% discount on your bill.")
else :
    print(f"To get 10% discount on your bill amount, it need to be greater than 1000")