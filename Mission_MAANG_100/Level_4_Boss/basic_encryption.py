user_input_text = input("Enter a text: ")

encrypted_text = ""

for each_char in user_input_text :
    ascii_number = ord(each_char)
    next_char = chr(ascii_number + 1)
    encrypted_text += next_char

print(f"Encrypted text {encrypted_text}")