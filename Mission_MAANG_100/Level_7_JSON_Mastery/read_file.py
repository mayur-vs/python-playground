import json

# File Handling
# File kabhi bhi write mode mein - open or create hoti hain
# json.dumps(python_object) - hum tab use karte hain jab, Python object ko JSON string mein convert karta hain
# json.dump(python_object, file_name) - hum tab use karte hain jab, json file mein write hain

# json.loads() - hum tab use karte hain jab, JSON String ko python mein convert karta hain
# json.load(file_name) - hum tab use karte hain jab, json file se read karna ho
with open("data.json", "r") as file:
    employee = json.load(file)

print(f"Name of Employee is {employee["name"]}")