def get_even_numbers(numbers_list : list) :
    even_nums_list = []

    for each_number in numbers_list :
        if each_number % 2 == 0 :
            even_nums_list.append(each_number)

    return even_nums_list

nums_list = [3, 1, 544, 2, 31, 12, 67, 8]
result_even_numbers_list = get_even_numbers(nums_list)
print(f"Here is a even numbers list : {result_even_numbers_list}")