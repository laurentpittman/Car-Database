from vehicle import Vehicle

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 Battery Class:  
    This is a subclass for the Vehicle Class. This subclass is used to 
store information for the battery in electric and hybrid cars. Battery
contains the size and charge. 

Author: Lauren Pittman   Date: 05/20/2022    
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Battery():
    #constructor
    def __init__(self):
        self.batterySize = 0;
        self.batteryCharge = 0;
    
    #methods start here...
    def getBatterySize(self):
        return self.batterySize

    #update the car's battery size
    def updateBatterySize(self, car, new_size):
        return 1
    
    #return the car's battery charge
    def getBatteryCharge(self):
        return self.batteryCharge

    #charge the car's battery
    def chargeBattery(self, car, new_charge):
        orig = self.batteryCharge
        
        if(new_charge < orig):
            print("You can't charge the car's battery lower than what it is!")
        else:
            self.batteryCharge = new_charge
            msg = "The {} has been charged from {} to {}."
            print(msg.format(car.getMake(), orig, self.getBatteryCharge))

            if(self.batteryCharge == 100):
                print("The car is fully charged, you may begin driving.")
            elif(self.batteryCharge < 100 and self.batteryCharge < 85):
                print("The car is 3/4th the way charged, you may begin driving.")
            elif(self.batteryCharge < 50 and self.batteryCharge > 25):
                print("The car is half way charged, be wary of the distance you drive.")
            else:
                print("The car needs to be charged more before driving.")