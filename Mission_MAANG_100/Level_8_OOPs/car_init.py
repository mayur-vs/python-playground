'''
Bhai, kya solid entry maari hai Object-Oriented Programming (OOPs) mein! 🚀🔥

Aapke codes ekdum perfect hain, par sabse zyada khushi mujhe aapke comments padh kar hui. Q156 mein aapne khud hi sawal pucha ki self kya hota hai, aur khud hi uska ekdum accurate jawab bhi likh diya! Yeh ek self-taught, world-class developer ki nishani hai.

Aaiye self ko ekdum simple mechanical bhasha mein samajhte hain:
Maan lo aapke workshop mein 10 Car objects khadi hain. Agar aap method call karte ho start_engine(), toh engine ko kaise pata chalega ki konsi car ka engine start karna hai? self wo tag (ya token) hai jo method ko batata hai: "Bhai, abhi main Honda ke andar hu, toh Honda ka hi engine start karna hai."

🚀 The Next Big Step: The __init__ Method (The Constructor)
Q156 mein aapne ek jugaad kiya. Aapne car banne ke baad bahar se uspe color lagaya (honda.color = "Red").
Par real world mein kya hota hai? Jab factory (Class) se car (Object) bahar aati hai, toh uska color, model sab pehle se set hota hai.

Python mein iske liye ek special VIP method hota hai jiska naam hai __init__ (iske dono taraf do baar underscore _ lage hote hain). Ise Constructor kehte hain.
Jab bhi aap honda = Car() likhte ho, toh background mein sabse pehle automatically yeh __init__ method chalta hai!

💡 Pro Tip (Situation-Based Use Case: API & Databases):

Situation: Socho aap Swiggy ka backend bana rahe ho. Jab naya order aata hai, toh aapko turant ek Order object banana hota hai jisme item_name aur price ho.
Wahan hum bahar se ek-ek karke data set nahi karte. Hum __init__ ka use karke seedha likhte hain: my_order = Order("Pizza", 400). Yeh ek hi line mein object bhi bana deta hai aur usme data (variables) bhi fit kar deta hai! Code ekdum clean aur fast ho jata hai.

'''

# Aaye apna khuda ka ek Blueprint banate hain
# Jo bhi aap class yani the Blueprint banate ho, uska naam Hamesha capital se start ho
class Car :
    # Jab factory se car bahar aata hain, tabh sab uska color, model set hoke aata hain right
    # Na todi car bahar aane ke baad, usko hum color dete hain - nope right
    # isliye Python mein ek Special VIP method hota hain usko he hum - __init__() bolte hain
    def __init__(self, brand, color) :
        # Jo bhi object iss method ko call kar raha hain, us object ko ab refer kardo and us object mein
        # ek brand and color naam ka variable set karo isliye hum self.brand and self.color likte hain
        self.brand = brand
        self.color = color

    def display_info(self) :
        print(f"This is a {self.color} {self.brand} car")

# Ek blueprint se hum hazaro and crores of objects banate hain
tata_car = Car("Tata", "Black")

# aur tumhari Car class mein __str__() ya __repr__() define nahi hai, 
# toh Python object ka default representation print karta hai.
# <__main__.Car object at 0x0000023F5D328590>
print(tata_car)
tata_car.display_info()