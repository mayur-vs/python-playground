user_input_number = int(input("Enter a number: "))

number_text = ""

for each_number in range(1, user_input_number + 1) :
    number_text += str(each_number)
    print(number_text)