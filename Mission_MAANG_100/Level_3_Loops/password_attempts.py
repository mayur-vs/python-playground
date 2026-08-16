counter = 1
user_password = "Abc12345"
while counter <= 3 :
    user_input_password = input("Enter your password: ")
    password_check = user_input_password == user_password

    if password_check :
        print(f"You have successfully logged in!")
        break
    else :
        if counter == 3 :
            print("All chances are over, please try again after 24 hours")
        else :
            print(f"This is your {counter} of 3, please try again")
    counter += 1

# Loop mereko 10 baar gumana hain, toh 100% 10 baar gumana chayiye - tabh for loop use karenge

# Loop mereko pata nhi kab takh chalega - Q ki hum malum hota hain tab tak chalega
# while loop hum tabh use karte hain for example - user se password lena hain, 3 baar maximum chance denge, so hume pata nhi ki user 1st attempt mein sahi password dalega ya 2nd attempt or 3rd attempt mein?
# lets say 3 chance dena but kabtak vo chalega pata nhi