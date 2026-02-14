# Activity 2: Adding methods to the Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
# Public method
    def set_make(self,make):
        self.make = make
    def set_model(self,model):
        self.model = model
    def set_year(self,year):
        self.year = year
    def __update_model(self, new_model):
        self.model = new_model
