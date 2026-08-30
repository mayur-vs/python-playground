'''
Maan lo aapne ek Vehicle class banayi jisme engine start aur stop ka code hai. 
Kal ko aapko Car aur Bike ki classes banani hain. 
Toh kya aap dono mein engine ka code dobara likhoge? Nahi! Hum Car ko Vehicle ka "Child" bana dete hain. 
Child class ko Parent class ki saari khubiyan (methods aur variables) muft mein mil jati hain. 
Isko Inheritance kehte hain.
'''

# aaye apna khud ka ek vehicle ka blueprint banate hain
class Vehicle : # isko parent class kahte hain
    # class mein jab bhi hum function banate hain tab usko hum method kahte hain
    # and uska first parameter self hota hain
    # self hum isliye likte hain, jab koi object uss method ko call karta hain toh self us object ko refer karta hain
    # yani background mein - Vehicle.start_engine(bullet_bike)
    def start_engine(self) :
        print(f"Engine start ho gya hain")

    def stop_engine(self) :
        print(f"Engine stop ho gya hain")

class Car(Vehicle) : # isko child class kahte hain
    def drive(self) :
        print(f"Car chal rahi hain")

class Bike(Vehicle) : # child class bolte hain
    def ride(self) :
        print(f"Bike Chal rahi hain")

# Car ka object banaya hain
car = Car()

car.start_engine()   # Vehicle se mila method
car.drive()          # Car ka apna method
car.stop_engine()    # Vehicle se mila method

print("----------------")

# Bike ka object
bike = Bike()

bike.start_engine()  # Vehicle se mila method
bike.ride()          # Bike ka apna method
bike.stop_engine()   # Vehicle se mila method