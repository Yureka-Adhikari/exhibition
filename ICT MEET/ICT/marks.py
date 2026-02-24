#Accept the marks of a student in 5 subjects and display the grade according to the following criteria:
#Average >= 90 : Grade A
#Average >= 80 and < 90 : Grade B
#Average >= 70 and < 80 : Grade C
#Average >= 60 and < 70 : Grade D
#Average < 60 : Grade F

m = int(input("Enter marks of subject 1: "))
s = int(input("Enter marks of subject 2: "))
e = int(input("Enter marks of subject 3: "))
n = int(input("Enter marks of subject 4: "))
c = int(input("Enter marks of subject 5: "))

avg = (m + s + e + n + c)/ 5

if avg >= 90:
    print("Grade A")
elif avg >= 80:
    print("Grade B")
elif avg >= 70:
    print("Grade C")
elif avg >= 60:
    print("Grade D")
else:
    print("Grade F")


