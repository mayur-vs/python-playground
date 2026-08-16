user_input_text = input("Enter a text: ")

spaces_count = 0

for each_char in user_input_text :
    if each_char == " " :
        spaces_count += 1

print(f"Spaces in your word is {spaces_count}")