#Activity 3: Hiding Data Attributes
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.__model = model
        self.year = year
