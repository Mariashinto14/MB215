#Activity1 Defining car class
class Car:
    def __init__(self, make, model, year):
        # private attribute
        self.make = make
        self.__model = model  
        self.year = year
    # Activity 2: Public method
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.__model}, Year: {self.year}")
    # Activity 2: Private method
    def __update_model(self, new_model):
        self.__model = new_model
    # Activity 4: __str__ method
    def __str__(self):
        return f"{self.year} {self.make} {self.__model}"
    #output of the car object when printed
    # Create a Car object
car = Car("Toyota", "Corolla", 2020)

  # Call the public method
car.display_info()

    
