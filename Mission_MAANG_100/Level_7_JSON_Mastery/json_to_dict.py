import json

# Muje Niche diye gaye dictionary ko internet par bejna hain, so use internet ki universal bhasha mein convert karke bejna padata hain
# internet ka universal basha hain JSON text format
# Jaise Amazon Lex Bot ne AWS Lambda ko data pass kar diya hain, vo data pass karne ke liye humko uss data ko text format yani JSON mein convert karke bejna padta hain

json_data = '{"name": "Mayur", "role": "Cloud Engineer", "skills": ["Python", "AWS"]}'

print(f"JSON Text Data : {json_data}")
print(f"Type of JSON Text Format is : {type(json_data)}")

py_object = json.loads(json_data)

print(f"Data of dictionary : {py_object}")
print(f"Type of dictionary is : {type(py_object)}")