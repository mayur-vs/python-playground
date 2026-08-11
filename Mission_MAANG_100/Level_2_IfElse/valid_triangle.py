# Take inputs from user and convert it into Integer
user_input_first_angle = int(input("Enter the First angle of triangle: "))
user_input_second_angle = int(input("Enter the Second angle of triangle: "))
user_input_third_angle = int(input("Enter the Third angle of triangle: "))

# Add all angles
sum_of_angles = user_input_first_angle + user_input_second_angle + user_input_third_angle

# Check sum_of_angles is equal to 180 or not
if sum_of_angles == 180 :
    print("Valid Triangle")
else :
    print("It's not a Valid Triangle")