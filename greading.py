# Ex2 :
# 1-> inputs--> subject, marks, max_marks
# percentage
# 90 -100  Grade(A+)
# 80 < 90  Grade(A)
# 70 < 80  Grade(B+)
# 60 < 70  Grade(B)
# 50 < 60  Grade(C)
# 40 < 50  Grade(D)
#    < 40  Fail
# Result:
# Subject : XXXX    Mark : XXXX     Grade : XX

# print(f"Subject : {subject}\tMark : {mark}\tGrade : {grade}")

subject = input("Enter Subject : ").capitalize()
max_marks = int(input("Enter max marks of subject : "))
marks = float(input("Enter subject marks : "))

if marks < 0 or marks > max_marks:
    print("Your inputs are wrong!")
    exit(0)

percent = (100 * marks) / max_marks

if percent >= 90:
    grade = "A+"
elif percent >= 80:
    grade = "A"
elif percent >= 70:
    grade = "B+"
elif percent >= 60:
    grade = "B"
elif percent >= 50:
    grade = "C"
elif percent >= 40:
    grade = "D"
else:
    grade = "Fail"

print(f"Subject : {subject}\tMark : {marks}\tGrade : {grade}")


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Welcome To The Board Result Portal\n Enter your Details below")
# subject=print(input("please enter subject :"))
# percentage=input("please enter your percentage :")
# print(percentage)

# if int(percentage)>90:
#     Grade = "A+"
#     print("Your Grade Is : A+")
# elif int(percentage)>80:
#     print("Your Grade Is : A ")
# elif int(percentage)>70:
#     print("Your Grade Is : B+")
# elif int(percentage)>60:
#     print("Your Grade Is : B")
# elif int(percentage)>50:
#     print("Your Grade Is : C+")
# elif int(percentage)>40:
#     print("Your Grade Is : C")
# else:
#     print("Your Result Is Fail")

# print(f"Subject:{subject}\t Mark:{percentage}\ Grade:{Grade}")
