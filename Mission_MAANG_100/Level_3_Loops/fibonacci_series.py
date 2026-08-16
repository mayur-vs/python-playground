first_place_number = 0
second_place_number = 1

fibonacci_series_text = ""

for i in range(1, 11) :
    fibonacci_series_text += str(first_place_number) +','
    first_place_number, second_place_number =  second_place_number, first_place_number + second_place_number

print(fibonacci_series_text.rstrip(','))