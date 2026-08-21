def atm_withdraw(balance : float, amount : int) :
    if amount <= 0 :
        return "Invalid Amount! Please enter a positive value." 
    elif amount > balance :
        return "Insufficient Funds"
    else :
        return balance - amount

result = atm_withdraw(amount = -50, balance = 110.2)
print(f"Result : {result}")