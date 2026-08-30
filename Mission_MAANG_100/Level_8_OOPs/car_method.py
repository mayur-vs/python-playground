# Aaye apna blueprint khud he banate hain

'''
Q155: Class ke andar Function (Method)

Suggested File Name: q155_car_method.py

Task: Car class ke andar ek function banao start_engine(self). (Class ke andar jab function banta hai, 
toh use Method kehte hain, aur uske bracket mein hamesha pehla word self aata hai). 
Is method mein print karo "Engine is starting... Vroom!".

Object banao honda = Car() aur engine start karo honda.start_engine().

'''

class Car :
    # Jab bhi hum class ke undar function banate hain, tab use Method bolte hain
    def start_engine(self) :
        print("Engine is starting... Vroom!")


# Ek blueprint se matlab ek class se hum lakhs of objects (The real thing) banate hain
honda = Car()

# Jab hum blueprint ya ni class se lakhs of objects banate hain tab use object mein
# uss object mein sab kuch aata hain automatic - data aur functions aata hain
honda.start_engine()