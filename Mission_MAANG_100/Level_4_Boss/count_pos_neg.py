numbers_list = [2, -2, 12, 3, -3, -0, 90, 13, -8]

count_of_positive_numbers = 0
count_of_negative_numbers = 0
count_of_zeros = 0

for each_number in numbers_list :
    if each_number < 0 :
        count_of_negative_numbers += 1
    elif each_number == 0 or each_number == -0 :
        count_of_zeros += 1
    else :
        count_of_positive_numbers += 1

print(f"Count of Positive Number: {count_of_positive_numbers}")
print(f"Count of Negative Number: {count_of_negative_numbers}")
print(f"Count of Zeros: {count_of_zeros}")