# Activity 1: Defining a Car class
#make is a public attribute, model is a private attribute, and year is a public attribute.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
#output of the car object when printed
car = Car("Toyota", "Corolla", 2020)
print(car.make, car.model, car.year)


