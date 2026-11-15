# method - is a function defined inside a class
# function - is a method defined outside a class

class Car: # user-defined data type(class) 
    def __init__(self, _brand, _model, _year, *args): # is called automatically when object creates
        # self - refers to the current object
        self.brand = _brand # attribute
        self.model = _model
        self.year = _year
        self.additional_information = args
        self.is_started = False

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Add.Info : {self.additional_information}")

    def start_stop(self):
        self.is_started = not self.is_started
        if(self.is_started):
            print("Engine has been started, vroom!")
        else:
            print("Engine has been stopped!")

car1 = Car("Merc", "E-klassen", 2020)
car2 = Car("BMW", "3 series", 2018, "4.0L", "2 doors")

car1.display_info()
car2.display_info()

car1.start_stop()
car1.start_stop()