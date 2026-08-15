# Take input from user and convert it into float
user_input_bill = float(input("Enter your bill amount: "))
user_restaurant_service_experience = input("How much you are happy with our service? ")

if user_restaurant_service_experience == 'Excellent' :
    adding_tip_into_user_bill = user_input_bill * 0.20
elif user_restaurant_service_experience == "Good" :
    adding_tip_into_user_bill = user_input_bill * 0.10
else :
    adding_tip_into_user_bill = user_input_bill * 0.05

user_total_bill = user_input_bill + adding_tip_into_user_bill
print(f"Here is your total bill: {user_total_bill} (includes tip)")