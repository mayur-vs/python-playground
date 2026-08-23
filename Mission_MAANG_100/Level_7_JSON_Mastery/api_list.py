import json

users = [{"name" : "Mayur" , "age" : 24}, {"name" : "Bill" , "age" : 24}]

json_array = json.dumps(users)
print(f"JSON Array/List : {json_array}")
print(type(json_array))