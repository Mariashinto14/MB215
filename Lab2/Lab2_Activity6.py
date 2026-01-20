# Get two numbers
num1 = float(input("Enter value of a: "))
num2 = float(input("Enter value of b: "))
# Calculate sum, difference, product, and quotient
sum  = num1 + num2
difference  = num1 - num2
product = num1 * num2
exponent = num1 ** num2
if num2 != 0:
    # 4. Division
    print(" num1 divided by num2 gives:", num1 / num2)

    # 5. Integer Division
    print("a divided by b for integer division gives:", num1 // num2)

    # 6. Remainder
    print("the remainder when num1 is divided by num2 is:", num1 % num2)
else:
    quotient = "undefined (division by zero)"
# Display results
print(" The sum is ", sum)
print(" The difference is ", difference)
print("Th product is :", product)
print("The quotient is:", quotient)
print("The exponentiation result (a^b):", exponent)