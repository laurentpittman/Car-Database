from vehicle import Vehicle
from battery import Battery

class HybridVehicle(Vehicle):
    #constructor
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        battery = Battery()
    
    #methods start here...