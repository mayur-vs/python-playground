user_input_day_number = int(input("Enter day number: "))

match user_input_day_number :
    case 0 :
        print("Sunday")

    case 1 :
        print("Monday")

    case 2 :
        print('Tuesday')

    case 3 :
        print("Wednesday")

    case 4 :
        print("Thursday")

    case 5 :
        print("Friday")

    case 6 :
        print("Saturday")

    case _ :
        print("Invalid Input enter number between 0 to 6")
    