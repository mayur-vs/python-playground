student = {
    "name"  : "mayur",
    "age"   : 23,
    "marks" : 85 
}

# del keyword use karke hum ek dictionary mein, ek key ko delete karna chahte hain toh vo delete hoga
# but key dictionary mein present rahta hain toh, tabh delete hoga
# but key dictionary mein nhi rahta hain toh vo KeyError dega
del student["age"]

print(student)