'''
Q156: Data aur Method ka Milan

Suggested File Name: q156_car_data.py

Task: Class ke methods apne andar data store kar sakte hain. 
Apni class mein ek variable dalo: honda.color = "Red". 
Fir ek naya method banao show_color(self) jisme print karo f"The car color is {self.color}". 
Use call karke dekho!
'''
# Aaye banate hain, apna blueprint khud hee banate hain
class Car :
    # jab bhi hum class ke undar function banate hain, tab usse hum method bolte hain
    # uss method ka pahla parameter self hota hain,
    # but muje ye pata nhi ki self naam ka parameter method ke undar kyu lika jaata hain
    def start_engine(self) :
        print("Engine is starting... Vroom!")

    # self isliye likte hain, ye self ye bata hain ki method kis object se ab kaam kar raha hain
    def show_color(self) :
        print(f"The car color is {self.color}")


# Ek blueprint ki madd se hum lakhs of Objects (the real thing) banate hain
honda = Car()

# har real thing mein yani object mein sab kuch automatic aata hain - methods, variables
honda.start_engine()

# class mein ek variable dalo: honda.color = "Red". 
# Q156 mein aapne ek jugaad kiya. Aapne car banne ke baad bahar se uspe color lagaya (honda.color = "Red").
# Par real world mein kya hota hai? Jab factory (Class) se car (Object) bahar aati hai, toh uska color, model sab pehle se set hota hai.
honda.color = "Red"
honda.show_color()