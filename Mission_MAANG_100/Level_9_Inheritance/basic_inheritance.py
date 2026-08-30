'''
Phase 4: Inheritance (Virasat) 🧬
Ab jab aapne Blueprint banana seekh liya hai, toh coding ka agla sabse bada rule samajhte hain: "Don't Repeat Yourself (DRY)".
Maan lo aapne ek Vehicle class banayi jisme engine start aur stop ka code hai. 
Kal ko aapko Car aur Bike ki classes banani hain. 
Toh kya aap dono mein engine ka code dobara likhoge? Nahi! Hum Car ko Vehicle ka "Child" bana dete hain. 
Child class ko Parent class ki saari khubiyan (methods aur variables) muft mein mil jati hain. 
Isko Inheritance kehte hain.
'''

# Aaye apna khuda ka ek blueprint banate hain - yani class banante hain
# ek blueprint se hum crores of objects yani the real thing bana sakte hain
# class ka naam capital se start hote hain
# python ke pass ek special VIP method hota hain - __init__(self) :

class Animal :
    # class mein jab hum function define karte hain
    # tab usko method kahte hain
    # method ka pahla paramter self hota hain
    # self ka matlab ye hota hain, jab koi object iss method call karta hain tab ye self uss object ko refer karta hain
    def speak(self) :
        print(f"Animal makes a sound")

# virasat - jab bhi hum parent class sab methods and variables child class mein use kar sakte hain
# usko programming mein Inheritance kahte hain

class Dog(Animal) :
    pass

my_dog = Dog()
my_dog.speak()