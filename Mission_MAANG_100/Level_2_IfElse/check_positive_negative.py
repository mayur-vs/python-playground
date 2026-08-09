# Yahan se computer aapse sirf math nahi karega,
# balki sochna shuru karega aur conditions ke hisaab se faisle lega!

user_input = int(input("Enter a number: "))

if user_input > 0 :
    print(f"{user_input} is a positive number.")
elif user_input < 0 :
    print(f"{user_input} is a negative number.")
else :
    print(f"{user_input} is neither positive nor negative. It is zero.")