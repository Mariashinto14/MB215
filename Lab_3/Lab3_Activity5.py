# assign initial values
total_sum = 0
count = 0

while total_sum < 100:
    user_input = input("Enter a number or space to stop: ")

    if user_input == "space":
        break
   
    number = float(user_input)
    total_sum += number
    count += 1

print("Total sum:", total_sum)
print("Numbers entered:", count)
