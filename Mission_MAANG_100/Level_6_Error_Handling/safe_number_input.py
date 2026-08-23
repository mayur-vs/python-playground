try :
    user_age = int(input("Enter a age: "))
    if user_age > 18 :
        print("You are Eligible for vote!")
    else :
        print("You are not Eligible for vote!")
except ValueError :
    print("Please enter a valid number, not text!")