#ask the user to input kilometers
kilometers = float(input("Enter the kilometers you want to convert to miles: "))

#conversion factor
miles = 0.621371 

#convert kilometers to miles
miles_converted = kilometers * miles

#display the converted miles
print(f"The converted miles is: {miles_converted:.2f}")