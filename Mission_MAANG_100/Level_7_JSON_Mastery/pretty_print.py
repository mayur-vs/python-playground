import json

employee = {"name": "Mayur", "role": "Cloud Engineer", "skills": ["Python", "AWS", "Git", "GitHub"]}

json_data = json.dumps(employee, indent=4)

print(f"JSON Data is ready to send over internet: {json_data}")