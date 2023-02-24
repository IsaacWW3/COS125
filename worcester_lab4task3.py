# Task 3
# This code calculates a student's average grade.
# 'None' grades indicate no submission was made. They should
# be treated as zeros.
# Drops the lowest grade.

mylist = [52, 0, 90, None, None]
total = 0
num_grades = 0
lowest_grade = 1000

for grade in mylist:
    if grade is None: # added if to make none 0
        grade = 0
        num_grades += 1 # added coutner to make num go up
    if grade:
        total += grade
        num_grades += 1
    if grade < lowest_grade:
        lowest_grade = grade


total -= lowest_grade

print(num_grades)
print(f"Average grade: {total/num_grades}")

