# Take input from user and convert it into float
weight_kg = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

# Convert height into meters
height_m = height_cm / 100

# Calculate bmi using Standard Metric Formula
bmi = (weight_kg / height_m ** 2)

# Display the result rounded to 2 decimal places
print(f"Your bmi is {bmi:.2f}")

# Categorize the BMI result
if bmi < 18.5 :
    print("Category: Underweight")
elif 18.5 <= bmi < 25 :
    print("Category: Normal weight")
elif 25 <= bmi < 30 :
    print("Category: Overweight")
else :
    print("Category: Obese")