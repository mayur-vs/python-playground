'''
super() kya karta hai?
Jab Child class ke andar tumhe Parent class ka method/constructor (__init__) call karna ho, 
tab super() use karte hain.

'''

class Vehicle :
    def __init__(self) :
        print("Parent class Vehicle ka constructor")

class Car(Vehicle) :
    def __init__(self) :
        # Jab bhi parent class ka Method/Constructor call karte hain tab hum super() use kar ke hum use karte hain
        super().__init__() # Parent class ka constructor call kiya hain
        print("Child class Car ka constructor")

honda_car = Car()