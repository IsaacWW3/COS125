# File: worcester_hw2b.py
# Author: Isaac Worcester
# Date: 2/2/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# Calculates weighted grade of student
# Collaboration:
# Me, Myself and I

hw_weight = float(input("Enter homework weight: "))
hw_grade = float(input("Enter homework grade: "))
pj_weight = float(input("Enter project weight: "))
pj_grade = float(input("Enter project grade: "))
lab_weight = float(input("Enter lab weight: "))
lab_grade = float(input("Enter lab grade: "))
eng_op_weight = float(input("Enter engagement opportunities weight: "))
eng_op_grade = float(input("Enter engagement opportunities grade: "))
hr_exm_weight = float(input("Enter hourly exam weight: "))
hr_exm_grade = float(input("Enter hourly exam grade: "))
fnl_exm_weight = float(input("Enter final exam weight: "))
fnl_exm_grade = float(input("Enter final exam grade: "))

hw_tot = hw_grade * hw_weight
pj_tot = pj_grade * pj_weight
lab_tot = lab_grade * lab_weight
eng_op_tot = eng_op_grade * eng_op_weight
hr_exm_tot = hr_exm_grade * hr_exm_weight
fnl_exm_tot = fnl_exm_grade * fnl_exm_weight

total_w = hw_tot + pj_tot + lab_tot + eng_op_tot + hr_exm_tot + fnl_exm_tot

print("Your grade is ", total_w)