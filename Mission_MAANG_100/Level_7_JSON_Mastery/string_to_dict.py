import json

data = '{"city": "Hyderabad", "temp": 30}'

py_dict = json.loads(data)

print(f"JSON Text Data converted into Python Dictionary : {py_dict}")