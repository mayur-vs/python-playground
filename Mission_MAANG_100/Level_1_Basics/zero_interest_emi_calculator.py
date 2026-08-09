user_loan_amount = float(input("Enter the loan amount: "))
user_loan_tenure = int(input("Enter the loan tenure (in months): "))
user_interest_rate = 0.0

if user_loan_tenure <= 0:
    print("Loan tenure must be greater than zero.")
else :
    result = user_loan_amount / user_loan_tenure
    print(f"The EMI for the loan is: {result:.2f}")