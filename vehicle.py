import random

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 Vehicle Class:  
    This is the parent class for Vehicle. This class is used to initialize
car objects in main.py. A vehicle contains a make, model, and year, as 
well as milage. In this class, the user can update the make, model, 
year, and milage in addition to getting any information from the
attributes listed above. 
   
    Child classes include: electricVehicle.py and hybridVehicle.py
    Subclasses include: battery.py

Author: Lauren Pittman   Date: 05/20/2022    
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Vehicle:

    car_db = []

    #constructor
    def __init__(self, make, model, year, price):
        self.carID = random.randint(0,10000)
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.milage = 0
    
    #creating a car
    def create(self):
        print("Enter in the following to create a car: ")
        car_make = input("Make: ")
        car_model = input("Model: ")
        car_year = input("Year: ")
        car_price = input("Price: ")
        car_milage = input("Milage: ")

        car = Vehicle(car_make, car_model, car_year, car_price)
        #place car into the database
        self.car_db.append(car)

        msg = "The {} {} has been placed into the database."
        print(msg.format(car.getYear(), car.getMake()))

    #store the car into the database
    def storeCar(self, car):
        self.car_db.append(car)
    
    #return the car's information
    def showInfo(self, car):
        msg = "ID: {}  {}   {}   {}   {}   ${}\n"
        print(msg.format(car.carID, car.make, car.model, car.year, car.milage, car.price))
    
    #print the list of cars
    def printList(self):
        if(len(self.car_db) == 0):
            print("There are no cars in the database.")
        else:
            print("\n")
            #print list of cars from the database
            for car in range(len(self.car_db)):
                self.car_db[car].showInfo(self.car_db[car])

    #return the car's make
    def getMake(self):
        return self.make
    
    #update the car's make
    def updateMake(self, car, new_make):
        orig = self.make
        self.make = new_make
        msg = "The {} make has been updated from {} to {}."
        print(msg.format(orig, orig, self.getMake()))

    #return the car's model
    def getModel(self):
        return self.model

    #update the car's model
    def updateModel(self, car, new_model):
        orig = self.model
        self.model = new_model
        msg = "The {} model has been updated from {} to {}."
        print(msg.format(orig, orig, self.getModel()))

    #return the car's year
    def getYear(self):
        return self.year

    #update the car's year
    def updateYear(self, car, new_year):
        orig = self.year
        self.year = new_year
        msg = "The {} make's year has been updated from {} to {}."
        print(msg.format(car.getMake(), orig, self.getYear()))

    #return the car's price
    def getPrice(self):
        return self.price
    
    #update the car's price
    def updatePrice(self, car, new_price):
        orig = self.price
        self.price = new_price
        msg = "The {} make's price has been updated from ${} to ${}."
        print(msg.format(car.getMake(), orig, self.getPrice()))     

    #return the car's milage
    def getMilage(self):
        return self.milage

    #update the car's milage
    def updateMilage(self, car, new_milage):
        orig = self.milage
        
        if(new_milage < orig):
            print("You can't lower the milage!")
        else:
            self.milage = new_milage
            msg = "The {}'s milage has been updated from {} to {}."
            print(msg.format(car.getMake(), orig, self.milage))

    #buy a car
    def buyCar(self, car):
        return 1

    #sell a car
    def sellCar(self, car):
        return 1
