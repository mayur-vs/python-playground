first_subject_marks = float(input("Enter marks for the first subject: "))
second_subject_marks = float(input("Enter marks for the second subject: "))
third_subject_marks = float(input("Enter marks for the third subject: "))

total_marks = first_subject_marks + second_subject_marks + third_subject_marks
average_marks = total_marks / 3

print(f"The average marks obtained in three subjects is: {average_marks:.2f}")