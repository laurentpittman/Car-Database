from vehicle import Vehicle
from battery import Battery

import datetime
date = datetime.datetime.now()

class Main():
    print(date)
    print("this is main.py running...\n")

    car1 = Vehicle("Ford", "Mustang", 1964)
    car1.updateMake(car1, "BOB")
    car1.updateYear(car1, 1999)
    car1.updateMilage(car1, 54)
    car1.updateMilage(car1, 28)
    car1.updateMilage(car1, 76)

    print("\n")
