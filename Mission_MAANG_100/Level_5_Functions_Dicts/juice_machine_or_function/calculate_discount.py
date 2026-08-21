def calculate_discount(price : float, discount_percent : float) :
    if discount_percent > 50 :
        print("Invalid discount")
        return 0
    else :
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price

result = calculate_discount(110.20, 59.4)
print(f"Result: {result:.2f}")