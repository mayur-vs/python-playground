user_input_seconds = int(input("Enter the number of seconds: "))

minutes = user_input_seconds // 60

remaining_seconds = user_input_seconds % 60

print(f"{user_input_seconds} seconds is equal to {minutes} minutes and {remaining_seconds} seconds.")