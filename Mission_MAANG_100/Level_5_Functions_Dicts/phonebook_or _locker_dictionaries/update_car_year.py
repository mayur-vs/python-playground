my_car = {
    "brand" : "Tata",
    "model" : "Harrier",
    "year"  : 2013,
    "color" : "Black"
}

# Dictionary mein add or update ka syntax same hota hain
# Dictionary ke undar vo key nhi rahta hain toh, vo new key create karta hain dictionary mein
# Dictionary ke undae key already rahta hain toh, vo uska value ko override kar deta hain

my_car["year"] = 2024

print(my_car)