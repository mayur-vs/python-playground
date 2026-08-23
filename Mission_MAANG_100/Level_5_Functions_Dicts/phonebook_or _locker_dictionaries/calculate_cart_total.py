def checkout_bill(cart) :
    total_price = 0
    for price in cart.values() :
        total_price += price
    return f"Your total bill is {total_price}"


user_cart = {"laptop": 50000, "mouse": 1000, "keyboard": 1500}
user_checkput_bill = checkout_bill(user_cart)
print(user_checkput_bill)