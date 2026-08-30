# aaye ab hum khud ek blueprint banate hain
# hum iss blueprint se hazaro or crores of objects yani - The real thing bana sakte hain


class Car :
    # Python mein special VIP method hain - yahi __init__() method
    # uska first parameter self hota hain
    # self hum is liye likte hain, jo object is method ko call kar raha hain
    # tab ye self us object ko refer karega
    def __init__(self, brand, color) :
        self.brand = brand
        self.color = color

    # Jab bhi class __str__() ya __repre__() define nhi hain
    # Python object ka default representation print karta hain
    # print(tata_car)
    # <__main__.Car object at 0x0000023F5D328590>
    '''
    Iska matlab roughly:

    __main__ → tumhari current Python file/program
    Car → object kis class ka hai
    object → ye ek object hai
    0x0000023F5D328590 → object ka memory-related address/reference representation

    '''

    # Agar tum chahte ho ki proper information print ho
    # Class mein __str__() method define kar do:

    def __str__(self) :
        return f"Car Brand : {self.brand}, Color : {self.color}"

tata_car = Car("Tata", "Black")
print(tata_car)