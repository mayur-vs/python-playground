for each_number in range(2, 51) :
    divisible_counter = 0
    for divisor in range(2, each_number) :
        if each_number % divisor == 0 :
            divisible_counter += 1
            break

    if divisible_counter == 0 :
        print(f"{each_number} is a prime number")