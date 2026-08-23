student = {
    "name"  : "mayur",
    "age"   : 23,
    "marks" : 85 
}

# dict.pop(keyname) use karke hum ek dictionary mein, ek key ko delete karna chahte hain toh vo delete hoga
# but key dictionary mein present rahta hain toh, tabh delete hoga
# but key dictionary mein nhi rahta hain toh vo KeyError dega
# ek benefit hain .pop() use karne se, vo humko deleted value return kar deta hain
deleted_keys_value = student.pop("age1", "Not Found Key")
print(student)
print(deleted_keys_value)