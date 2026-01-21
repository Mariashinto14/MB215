# Get two numbers
num1 = float(input("Enter value of a: "))
num2 = float(input("Enter value of b: "))

# Calculations
addition = num1 + num2
difference = num1 - num2
product = num1 * num2
exponent = num1 ** num2

if num2 != 0:
    quotient = num1 / num2
    int_division = num1 // num2
    remainder = num1 % num2
else:
    quotient = "undefined (division by zero)"
    int_division = "undefined"
    remainder = "undefined"

# Display results
print("The sum is:", addition)
print("The difference is:", difference)
print("The product is:", product)
print("The quotient is:", quotient)
print("The integer division result is:", int_division)
print("The remainder is:", remainder)
print("The exponentiation result (a^b) is:", exponent)
