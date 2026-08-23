counts_dict = {}

user_input_text = input("Enter a word: ")

for each_character in user_input_text :
    if each_character in counts_dict :
        counts_dict[each_character] += 1
    else :
        counts_dict[each_character] = 1

print(f"'{user_input_text}' : {counts_dict}")