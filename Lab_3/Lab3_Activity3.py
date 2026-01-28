#ask the user to input cylinder dimensions
diameter = float(input("Enter the diameter of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

#calculate the volume of the cylinder
pi = 3.1416
print(f"The value of pi is: {pi:.2f}")

radius = diameter / 2
volume = pi * (radius ** 2) * height
#print the volume of the cylinder
print(f"The volume of the cylinder is: {volume}")