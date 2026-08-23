import json

try :
    bad_data = "{name: Mayur}"
    json.loads(bad_data)
except json.JSONDecodeError :
    print("please check ur JSON format")