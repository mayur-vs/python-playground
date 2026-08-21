def find_maximum(numbers_list : list) :
    maximum_number = numbers_list[0]

    for each_number in numbers_list :
        if each_number > maximum_number :
            maximum_number = each_number
    return maximum_number

nums_list = [3, 4, 544, 2, 44, 12, 67, 8]
result_max_number = find_maximum(nums_list)
print(f"Maximum number in {nums_list} list is {result_max_number}")