def calculate_grade(marks):
    # Marks ke hisab se grade calculate karna
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

# Student ke details input lena
name = input("Enter student's name: ")
roll_number = input("Enter student's roll number: ")
marks_1 = float(input("Enter marks for subject 1: "))
marks_2 = float(input("Enter marks for subject 2: "))
marks_3 = float(input("Enter marks for subject 3: "))

# Marks ka average calculate karna
average_marks = (marks_1 + marks_2 + marks_3) / 3

# Grade calculate karna
grade = calculate_grade(average_marks)

# Grade card print karna
print("************* Grade Card *************")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Subject 1 Marks: {marks_1}")
print(f"Subject 2 Marks: {marks_2}")
print(f"Subject 3 Marks: {marks_3}")
print(f"Average Marks: {average_marks}")
print(f"Grade: {grade}")
print("**************************************")