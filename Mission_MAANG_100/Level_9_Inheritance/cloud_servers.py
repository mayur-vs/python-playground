# Aaye apna khuda ka ek blueprint banate hain - yani class banante hain
# ek blueprint se hum crores of objects yani the real thing bana sakte hain
# class ka naam capital se start hote hain
# python ke pass ek special VIP method hota hain - __init__(self) :

class CloudServer : # Parent Class
    # class mein jab hum function define karte hain
    # tab usko method kahte hain
    # method ka pahla paramter self hota hain
    # self ka matlab ye hota hain, jab koi object iss method call karta hain tab ye self uss object ko refer karta hain
    
    def __init__(self, ip_address) :
        self.ip_address = ip_address
    
    def start_server(self) :
        print(f"Server started...{self.ip_address}")

# virasat - jab bhi hum parent class sab methods and variables child class mein use kar sakte hain
# usko programming mein Inheritance kahte hain

class DatabaseServer(CloudServer) : # Child Class
    # __init__(self, ip_address) -- init method by default access kar sakte hain
    def connect_db(self) :
        print("DB sever started...")

dynamoDB = DatabaseServer("127.0.0.1")
dynamoDB.start_server()
dynamoDB.connect_db()