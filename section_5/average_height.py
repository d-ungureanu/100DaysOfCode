# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
# DO NOT USE len() and/or sum()
sum_of_heights = 0
number_of_students = 0
for entry in student_heights:
    sum_of_heights += entry
    number_of_students += 1
average_height = sum_of_heights / number_of_students
print(round(average_height))
