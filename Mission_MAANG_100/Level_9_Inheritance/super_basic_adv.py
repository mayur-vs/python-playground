# aaye hum super() ka concept samajate hain
class Parent :
    def greet(self) :
        print("Hello from Parent")

class Child(Parent) :
    def greet(self) : # method override ho raha hain
        super().greet() # Parent class ka method ko call kar rahe hain super() use karke
        print("Hello from Child")

child_object = Child()
child_object.greet()