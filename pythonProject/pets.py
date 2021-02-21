# creating class named pets:

class pets:

    def __init__ (self,n,a,h,p):
        self.name=n
        self.age=a
        self.hunger=h
        self.playful=p

    def getName(self):
        return self.name
    def getage(self):
        return self.age
    def gethunger(self):
        return self.hunger
    def getplayful(self):
        return self.playful

    def setname(self,n):
        self.name=n
    def setage(self,a):
        self.age=a
    def sethunger(self,h):
        self.hunger=h
    def setplayful(self,p):
        self.playful=p

pets1=pets('sam',2,False,True)
print(pets1.getName())
print(pets1.getage())
print(pets1.gethunger())
print(pets1.getplayful())
pets1.setname('tiger')
print(pets1.getName())