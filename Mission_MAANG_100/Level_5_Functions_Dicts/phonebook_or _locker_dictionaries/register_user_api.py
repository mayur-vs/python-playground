import random

def register_user(name, email) :
    random_number = random.randint(1000, 9999)
    print(random_number)
    user_profile_dict = {
        "user_id" : random_number,
        "user_name" : name,
        "user_email" : email
    }
    return user_profile_dict

user_name_input = input("Enter a user name: ")
user_email_input = input("Enter a user email: ")
user_profile = register_user(user_name_input, user_email_input)
print(f"Here is your user profile ready to save in DynamoDB : {user_profile}")