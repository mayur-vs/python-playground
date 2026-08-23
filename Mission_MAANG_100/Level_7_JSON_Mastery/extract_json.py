import json

text_data = '{"city": "Pune", "temp": 30}'

py_dict = json.loads(text_data)

print(f"City name is : {py_dict['city']}")