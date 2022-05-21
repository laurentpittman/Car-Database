from vehicle import Vehicle
from electricVehicle import ElectricVehicle
from hybridVehicle import HybridVehicle
from battery import Battery

import datetime
import random

date = datetime.datetime.now()

class Main():
    print(date)
    print("Welcome to Cars.com! Buy and sell any cars. \n")

    try:
        answer = input("\nAre you a (1)customer or (2)employee? ")

        make, model, year, price = 0, 0, 0, 0
        #initialize empty car object
        car = Vehicle(make,model,year,price)

        #add pre-existing car to database
        car1 = Vehicle("Hyundai", "Accent", 2020, 16000)
        car1.storeCar(car1)
        car2 = Vehicle("Toyota", "Camry", 2018, 18500)
        car2.storeCar(car2)
        car3 = Vehicle("Honda", "Accord", 2020, 25000)
        car3.storeCar(car3)

        car3.updateMake(car3, "Cheevy")
        car3.updateModel(car3, "Bolt")

        #create a while loop for a employee
        user_input = True
    
        if(answer == "1"):
            while(user_input):
                print("\n  1. get car info\n  2. buy a car\n  3. sell a car\n  4. quit")
                answer = input("\nINPUT: ")

                #get car info
                if(answer == '1'):
                    #finish -> print list
                    car.showInfo()

                #buy a car
                elif(answer == '2'):
                    car.buyCar()

                #sell a car
                elif(answer == '3'):
                    car.sellCar()

                elif(answer == '4'):
                    user_input = False #exit the program

                else:
                    print("Invalid input: try again.")
        
        #create a while loop for a employee
        elif(answer == "2"):
            while(user_input):
                line1 = "  1. create car\n  2. display cars\n  3. get complete car info"
                line2 = "  4. update car\n  5. find cars\n  5. delete car\n  6. exit\n"

                print(line1)
                print(line2)
                answer = input("INPUT: ")

                #create a car and place in into the list
                if(answer == '1'):
                    car.create()

                elif(answer == '2'):
                    car.printList()

                elif(answer == '3'):
                    #car.showInfo()
                    print("*")
                    car.showInfo(car) 

                elif(answer == '4'):
                    car.printList()
                    answer = int(input("Enter ID you want to change: "))
                    #iterate through list to find car ID
                    for car in Vehicle.car_db:
                        print(car.getCarID())
                        #check if car ID is in the database
                        if car.getCarID() == int(answer):
                            car.updateCar(car)
                            break

                elif(answer == '5'):
                    print("hi")
                    
                elif(answer == '6'):
                    user_input = False
                
                else:
                    print("Invalid input: try again.")
    
    except KeyboardInterrupt:
        print("\n")
        exit(0)