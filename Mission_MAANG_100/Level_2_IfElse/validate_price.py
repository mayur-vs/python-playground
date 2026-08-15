user_input_product_price = float(input("Enter a product price: "))

if user_input_product_price < 0 :
    print("Invalid Price")
else :
    print(f"Your product price is {user_input_product_price:.2f}")