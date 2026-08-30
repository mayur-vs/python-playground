# aaye ab hum khud ek blueprint banate hain
# hum iss blueprint se hazaro or crores of objects yani - The real thing bana sakte hain


class Car :
    pass


tata_car = Car()
print(tata_car)

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