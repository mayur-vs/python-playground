# Aaye hum khud ka ek class/blueprint banate hain 

class Employee :
    def __init__(self, name) :
        self.name = name

class Manager(Employee) :
    def __init__(self, name, department) :
        super().__init__(name)
        self.department = department

mayur_manager = Manager("Mayur", "IT")