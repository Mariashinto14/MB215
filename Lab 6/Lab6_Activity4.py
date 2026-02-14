class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.__model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.__model}"
#output of the car object when printed
car = Car("Toyota", "Corolla", 2020)
print(car)