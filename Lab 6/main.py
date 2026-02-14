# main.py

from Car import Car

def compare_car_years(car1, car2):
    return car1.year < car2.year

# Create Car objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

# Display car information
car1.display_info()
car2.display_info()

# Compare years
if compare_car_years(car1, car2):
    print("Car 1 is older than Car 2")
else:
    print("Car 1 is newer than or the same age as Car 2")

# Print using __str__
print(car1)
print(car2)
