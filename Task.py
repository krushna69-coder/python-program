name = input("Enter student name: ")
m1 = int(input("Enter marks of M1: "))
m2 = int(input("Enter marks of M2: "))
m3 = int(input("Enter marks of M3: "))
spos = int(input("Enter marks of SPOS: "))
dbms = int(input("Enter marks of DBMS: "))
cg = int(input("Enter marks of CG: "))

total_marks = m1 + m2 + m3 + spos + dbms + cg
max_marks = 600 

if m1 >= 34 and m2 >= 34 and m3 >= 34 and spos >= 34 and dbms >= 34 and cg >= 34:
    percentage = (total_marks / max_marks) * 100
    
    if percentage > 90:
        grade = "A"
    elif percentage > 85:
        grade = "B"
    elif percentage > 75:
        grade = "C"
    else:
        grade = "Pass"

    
    print(f"Hello {name},")
    print(f"Total Marks: {total_marks}/{max_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Your grade is: {grade}")
else:
    print(f"Hello {name},")
    print(f"Total Marks: {total_marks}/{max_marks}")
    print("You have failed in one or more subjects.")
    print("Percentage and grade cannot be calculated.")

