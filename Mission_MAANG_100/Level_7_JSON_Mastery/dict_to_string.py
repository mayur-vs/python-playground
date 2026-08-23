import json

employee = {"name": "Mayur", "role": "Dev"}

json_data = json.dumps(employee, indent=4)

print(f"JSON Text String is ready to send over internet: {json_data}")