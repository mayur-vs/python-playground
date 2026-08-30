# Aaye hum khud ka Product class or blueprint banate hain
# iss blueprint se hum crores of product objects banate hain

class Product :
    # Python mein ek special VIP method hota hain - __init__() method
    # Class ke methods ke under hum data ko set karte hain
    # class ke methods ka first parameter self hota hain
    # __init__(self) - ye init method Python class ka heart hain 
    # self ye hain ki, jis bhi object iss method ko call kar raha hain, us object ko refer karta hain

    def __init__(self, product_name, product_price) :
        self.product_name = product_name
        self.product_price = product_price

    def apply_discount(self, discount_amount) :
        if discount_amount > self.product_price :
            print(f"We cannot apply discount amount bcoz Discount amount is greater than Product price")
        else :
            new_product_price_after_discount_applied = self.product_price - discount_amount 
            print(f"You total amount is {new_product_price_after_discount_applied} after {discount_amount} discount is applied. Thanks for shopping!")


lenovo_laptop = Product("Lenevo Laptop", 211000)
lenovo_laptop.apply_discount(4000)