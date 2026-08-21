def check_password_strength(password : str) :
    return "Weak" if len(password) < 8 else "Strong"

user_input_password = input("Enter a password: ")
result = check_password_strength(user_input_password)
print(result)