
from errno import ECOMM
from math import dist
from pydoc import describe


class Car:
    def __init__(self, **kwargs):
        self.engine_on = kwargs["engine_on"]
        self.fuel = kwargs["fuel"]
        self.is_electric = kwargs["electric"]
        self.is_manual = kwargs["manual"]
        self.km = 0
        self.charge = 100
        self.speed = 0
        self.gear = "Neutral"
        self.clutch = "Up"
        self.economy = 12  # 12 km / liter

    def status(self):
        print(self.__dict__)

    def drive(self, distance):
        required_fuel = distance/self.economy
        if required_fuel > self.fuel:
            self.km += (self.fuel*distance)/self.economy
            return self.km
        if self.is_manual and self.gear == "First":
            self.km += distance
            return self.km

    # def shift_gear(self, num):
     #   if self.


car1 = Car(engine_on=False)
#car2 = Car(150, True, "Mazda")
#car3 = Car()
# car3.status()
