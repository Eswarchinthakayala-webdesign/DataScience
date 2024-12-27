class Vehicle:
    def general_usage(self):
        print("General Usage: Transportation")
class Car(Vehicle):
    def __init__(self):
        print("I'm Car")
        self.wheels=4
        self.has_roof=True
    def specific_usage(self):
        print("specific use: long distance travel with family/friends")
class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm Motor Cycle")
        self.wheels=2
        self.has_roof=False
    def specific_usage(self):
        print("specific use: long distance ride with single person")

car=Car()
car.general_usage()
car.specific_usage()

mc=MotorCycle()
mc.general_usage()
mc.specific_usage()
