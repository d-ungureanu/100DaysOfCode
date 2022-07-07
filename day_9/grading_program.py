student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}

grade = ""
for student in student_scores:
    score = student_scores[student]
    if score in range(91, 101):
        grade = "Outstanding"
    elif score in range(81, 91):
        grade = "Exceeds Expectations"
    elif score in range(71, 81):
        grade = "Acceptable"
    elif score < 71:
        grade = "Fail"
    student_grades[student] = grade

# 🚨 Don't change the code below 👇
print(student_grades)
