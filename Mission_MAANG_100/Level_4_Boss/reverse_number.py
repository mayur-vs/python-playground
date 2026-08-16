user_input_number = input("Enter a number: ")

reverse_text_number = ""

for each_char_index in range(len(user_input_number) -1, -1, -1) :
    reverse_text_number += user_input_number[each_char_index]

print(f"Reversed number is {reverse_text_number}")
# print(user_input_number[::-1])
