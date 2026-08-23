import json

# Muje Niche diye gaye dictionary ko internet par bejna hain, so use internet ki universal bhasha mein convert karke bejna padata hain
# internet ka universal basha hain JSON text format
# Jaise Amazon Lex Bot ne AWS Lambda ko data pass kar diya hain, vo data pass karne ke liye humko uss data ko text format yani JSON mein convert karke bejna padta hain
employee = {"name": "Mayur", "role": "Cloud Engineer", "skills": ["Python", "AWS", "Git", "GitHub"]}
print(f"Data of dictionary : {employee}")
print(f"Type of dictionary is : {type(employee)}")

json_data = json.dumps(employee, indent=4)

print(f"JSON Text Data : {json_data}")
print(f"Type of JSON Text Format is : {type(json_data)}")