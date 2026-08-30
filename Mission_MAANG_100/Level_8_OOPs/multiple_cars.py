# Aaye hum khud ka ek class/blueprint banate hain
# iss the blueprint se hum crores of objects banate hain

class Car :
    # python mein ek special VIP method hota hain - __init__()
    # jab aap ek blueprint se ek object ya ni the real thing banoge
    # tab ye sabse pahle __init__() method call hota hain background mein
    # issi __init__() method ko programming basha mein constructor bola jata hain
    # Class ke methods apne andar data store kar sakte hain.
    # yani class ke methods ko ye ability hain vo data store kar sakta hain
    def __init__(self, brand, color) :
        self.brand = brand
        self.color = color

    def display_info(self) :
        print(f"This is a {self.color} {self.brand} car")

tata_car = Car("Tata", "Red")
honda_car = Car("Honda", "Blue")
ford_car = Car("Ford", "Violet")

tata_car.display_info()
honda_car.display_info()
ford_car.display_info()