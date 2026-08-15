user_input_year = input("Enter a year: ")

if not user_input_year.isdigit():
    print("Invalid year! re-enter a valid year")
else:
    user_input_year = int(user_input_year)
    user_input_month_name = input("Enter a Name of the Month: ")
    is_leap_year = ((user_input_year % 4 == 0) and (user_input_year % 100 != 0)) or (user_input_year % 400 == 0)

    match user_input_month_name.lower():
        case 'january':
            print("31 days in January Month")

        case 'february':
            if is_leap_year:
                print("29 days in February Month")
            else:
                print("28 days in February Month")

        case 'march':
            print("31 days in March Month")

        case 'april':
            print("30 days in April Month")

        case 'may':
            print("31 days in May Month")

        case 'june':
            print("30 days in June Month")

        case 'july':
            print("31 days in July Month")

        case 'august':
            print("31 days in August Month")

        case 'september':
            print("30 days in September Month")

        case 'october':
            print("31 days in October Month")

        case 'november':
            print("30 days in November Month")

        case 'december':
            print("31 days in December Month")

        case _:
            print("Invalid month name! re-enter a valid month name")
