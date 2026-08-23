prices = {
    "mango"  : 40,
    "banana" : 120,
    "apple"  : 12
}

# for item in prices.items() :
#     print(f"The price of {item[0]} is {item[1]}")

for fruit_name, fruit_price in prices.items() :
    print(f"The price of {fruit_name} is {fruit_price}.")