user_input_age = int(input("Enter your age: "))

if 0 <= user_input_age <= 12 :
    print(f"Your are Child and your ticket price is 50 rupees")
elif 13 <= user_input_age <= 17 :
    print(f"Your are Teenager and your ticket price is 60 rupees")
elif 18 <= user_input_age <= 59 :
    print(f"Your are Adult and your ticket price is 100 rupees")
elif user_input_age >= 60 :
    print(f"Your are Senior and your ticket price is 70 rupees")
else :
    print("Invalid age! Age cannot be negative")