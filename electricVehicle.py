from vehicle import Vehicle
from battery import Battery

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 ElectricVehicle Class:  
    This is a child class for the Vehicle Class. This class is used to 
create electric vehicles.

Author: Lauren Pittman   Date: 05/20/2022
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class ElectricVehicle(Vehicle):
    #constructor
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        battery = Battery()
    
    #methods start here...
    