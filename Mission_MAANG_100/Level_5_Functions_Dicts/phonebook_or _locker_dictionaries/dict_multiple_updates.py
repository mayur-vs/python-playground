order_details = {
    "item"  : "Pizza",
    "size"  : "Regular",
    "crust" : "Thin"
}

print(order_details)

# Ek saath multiple keys ko add or update karna using .update() method
order_details.update({"size" : "Large", "extra_cheese" : True, "price" : 450})
print(order_details)