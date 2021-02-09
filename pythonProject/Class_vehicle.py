# CLASS VEHICLE

from termcolor import colored,cprint
import random
from random import randint,choices,sample

class vehicle:
    def __init__(self,make,model,year, weight, Needsmaintenance=False,TripsSinceMaintenance=0):
        self.make=make
        self.model=model
        self.year=year
        self.weight=weight
        self.Needsmaintenance=Needsmaintenance
        self.TripsSinceMaintenance=TripsSinceMaintenance
    #getters
    def getmake(self):
        return self.make

    def getmodel(self):
        return self.model

    def getyear(self):
        return self.year

    def getweight(self):
        return self.weight

    def getNeedsmaintenance(self):
        return self.Needsmaintenance

    def getTripsSinceMaintenance(self):
        return self.TripsSinceMaintenance


    def repair(self):
        self.Needsmaintenance=False
        self.TripsSinceMaintenance=0




class cars(vehicle):
    def __init__ (self,m,mo,year,weight,Needsmaintenance=False,TripsSinceMaintenance=0,isDriving=False):
        vehicle.__init__ (self,m,mo,year,weight,Needsmaintenance,TripsSinceMaintenance)
        self.isDriving=isDriving

    def drive(self):
        self.isDriving=True

    def stop(self):
        if self.isDriving:
            self.TripsSinceMaintenance+=1
            if self.TripsSinceMaintenance>100:
                self.Needsmaintenance=True
        self.isDriving=False

class plane(vehicle):
    def __init__(self, m, mo, year, weight,Needsmaintenance=False,TripsSinceMaintenance=0, isFlying=False):
        vehicle.__init__(self, m, mo, year, weight,Needsmaintenance,TripsSinceMaintenance)
        self.isFlying = isFlying

    def Flying(self):
        if self.Needsmaintenance==True:
            return False
        self.isFlying=True
        return True


    def landing(self):
        if self.isFlying:
            self.TripsSinceMaintenance += 1
            if self.TripsSinceMaintenance > 100:
                self.Needsmaintenance = True
        self.isFlying=False

    def repair(self):
        self.Needsmaintenance = False
        self.TripsSinceMaintenance = 0


def CAR_DETAILS (wheeler):
    cprint('='*20, 'magenta')
    cprint('CAR-DETAILS', 'blue', 'on_yellow', attrs=['bold'])
    print('MAKE:', colored(wheeler.make, 'green'))
    print('MODEL:', colored(wheeler.model, 'green'))
    print('YEAR:', colored(wheeler.year, 'green'))
    print('WEIGHT:', colored(wheeler.weight, 'green'))
    print("NEEDMAINTENANCE:", colored(wheeler.Needsmaintenance, 'green'))
    print('TRIP_SINCE_MAINTENANCE:', colored(wheeler.TripsSinceMaintenance, 'green'))


def PLANE_DETAILS (planer):
    cprint('='*20, 'magenta')
    cprint('PLANE-DETAILS', 'magenta', 'on_blue', attrs=['bold'])
    print('MAKE:', colored(planer.make, 'green'))
    print('MODEL:', colored(planer.model, 'green'))
    print('YEAR:', colored(planer.year, 'green'))
    print('WEIGHT:', colored(planer.weight, 'green'))
    print("NEEDMAINTENANCE:", colored(planer.Needsmaintenance, 'green'))
    print('TRIP_SINCE_MAINTENANCE:', colored(planer.TripsSinceMaintenance, 'green'))

def random_mode(wheeler):
    ch=random.randint(1,101)
    # choice=random.sample(list,k=1)
    # choice=random.choice(list)
    for i in range(ch):
        wheeler.drive()
        wheeler.stop()

def random_planemode(planes,choice=None):
    ch = random.randint(1, 106)

    for i in range(1,ch):
        flying=planes.Flying()
        if flying:
            planes.landing()
        else:
            cprint("Boeing {0} can't fly due to the requirement of maintenance".format(colored(planes.model,'blue')), 'red')
            cprint('Repairing......', 'blue')
            planes.repair()

# Creating 3 different car instances
wheeler_one =cars('Tesla', 'MODEL S', 2012,'4766 lbs')
wheeler_two =cars('Tesla','MODEL 3', 2011,'4654 lbs')
wheeler_three=cars('Tesla','MODEL x', 2010,'4555 lbs')

#Creating 2 different plane instances
plane_one=plane('Boeing', 737, 1967, '85,000 kg')
plane_two=plane('Boeing', 727, 1964, '84,000 kg')


#Interchanging the drive and stop mode frequently
random_mode(wheeler_one)
random_mode(wheeler_two)
random_mode(wheeler_three)
random_planemode(plane_one)
random_planemode(plane_two,105)

#printing out the car details

CAR_DETAILS(wheeler_one)
CAR_DETAILS(wheeler_two)
CAR_DETAILS(wheeler_three)
PLANE_DETAILS(plane_one)
PLANE_DETAILS(plane_two)