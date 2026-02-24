import os
import tkinter as tk
from tkinter import messagebox, simpledialog 

if not os.path.exists('digital report cards'):
    os.makedirs('digital report cards')

n = int(input("Enter the number of students: "))

students = []
grades = []

for i in range(n):
    name = input(f"Enter the name of student {i+1}: ")
    grades = []
    total = 0
    for j in range(3):
        grade = float(input(f"Enter grade {j+1} for {name}: "))
        grades.append(grade)
        total += grade
    average = total / 3
    if average >= 90:
        print("Grade: A")
        letter_grade = "A"
    elif average >= 80:
        print("Grade: B")
        letter_grade = "B"
    elif average >= 70:
        print("Grade: C")
        letter_grade = "C"
    elif average >= 60:
        print("Grade: D")
        letter_grade = "D"
    else:
        print("Grade: F")
        letter_grade = "F"
    
    print(f"The average grade for {name} is: {average}")

    content = f"Name: {name}\nGrades: {grades}\nAverage: {average}\nGrade: {letter_grade}\n"
    filename = f"digital report cards/{name.replace(' ', '_')}_report.txt"
    count = 1
    while os.path.exists(filename):
        filename = f"digital report cards/{name.replace(' ', '_')}_report_{count}.txt"
        count += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Report card saved as {filename}")
 