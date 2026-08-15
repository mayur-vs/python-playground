bank_account_balance = 5000

user_withdrawal_amount = int(input("Enter amount to withdraw: "))

if user_withdrawal_amount > bank_account_balance :
    print("Insufficient funds")
else :
    print(f"Here is your withdrawal {user_withdrawal_amount} amount.")
    print(f"Your remaining balance is {bank_account_balance - user_withdrawal_amount}. Thank you!")