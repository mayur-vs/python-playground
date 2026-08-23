import json

with open("data.json", "r") as file :
    employee = json.load(file)

employee["status"] = "Active"

with open("data.json", "w") as json_file :
    json.dump(employee, json_file, indent=4)