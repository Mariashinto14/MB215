#ask the user to input numeric grade
nGrade = float(input("Enter your numberic grade: "))

#convering numeric grade to letter grade
if nGrade >= 90:
    Igrade = "A+,You did amazing job!"
elif nGrade >= 80:
    Igrade = "A,Great job!"
elif nGrade >= 70:
    Igrade = "B,Good job!"
elif nGrade >= 60:
    Igrade = "C,You passed!"
elif nGrade >= 50:
    Igrade = "D,You barely passed!"
else:
    Igrade = "F"
#printing the letter grade
print(f"Your letter grade is {Igrade}")