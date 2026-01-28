# Boolean variables
pink = True
blue = False

#Step 2: Demonstrate logical operations (AND, OR, NOT)

# Logical AND
print("pink AND blue:", pink and blue)
# Logical OR
print("pink OR blue:", pink or blue)
# Logical NOT
print("NOT pink:", not pink)
print("NOT blue:", not blue)

# Step 3: Use a Boolean variable in a conditional statement

# AND condition
if pink and blue:
    print(" Both pink and blue are True.")
elif pink and not blue:
    print("Pink is True but blue is False.")
else:
    print("both is False.")

# OR condition
if pink or blue:
    print(" At least one of pink or blue is True.")
else:
    print(" Both pink and blue are False.")

# NOT condition
if not pink:
    print(" Pink is False.")
elif not blue:
    print("Blue is False.")
else:
    print("Both are True.")
