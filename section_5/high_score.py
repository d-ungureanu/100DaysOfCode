# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# DO NOT USE max()
high_score = student_scores[0]
for entry in student_scores:
    if entry > high_score:
        high_score = entry
print(f"The highest score in the class is: {high_score}")
