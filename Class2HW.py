grade = int(input("Enter the grade: "))
if grade >= 80:
    grade = "A"
elif grade >= 75:
    grade = "B+"
elif grade >= 70:
    grade = "B"
elif grade >= 65:
    grade = "C+"
elif grade >= 60:
    grade = "C"
elif grade >= 55:
    grade = "D+"
elif grade >= 50:
    grade = "D"
elif grade < 50:
    grade = "F"
print("Your grade is: ", grade)