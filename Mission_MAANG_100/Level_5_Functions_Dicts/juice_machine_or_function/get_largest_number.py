def get_largest(number_one: int, number_two: int) :
    if number_one > number_two :
        largest_number = number_one
    else :
        largest_number = number_two
    return largest_number

result = get_largest(10, 21)
print(f"Result: {result}")