class Vehicle:
    #constructor
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.milage = 0
    
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
