prices = {
    "mango"  : 40,
    "banana" : 120,
    "apple"  : 12
}

for fruit_name, fruit_price in prices.items() :
    if fruit_price > 50 :
        print(f"Price of {fruit_name} is greater than 50")