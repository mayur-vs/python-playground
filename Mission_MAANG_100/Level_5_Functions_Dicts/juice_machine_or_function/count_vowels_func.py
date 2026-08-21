def count_vowels(word : str) :
    vowels_count = 0

    for each_char in word :
        if each_char in "AEIOUaeiou" :
            vowels_count += 1

    return vowels_count

user_input_string = input("Enter a word: ")
print(f"Vowel in your word is {count_vowels(user_input_string)}")