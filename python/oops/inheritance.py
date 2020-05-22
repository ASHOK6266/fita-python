class airlineManufacturer:

    #class attributes
    category = "Arlines"

    #instance attributes
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def speedVerify(self):
        print("{} has max speed of {}",format(self.name,self.speed))


#Single inheritance
class airBus(airlineManufacturer):

    def __init__(self):
        super().__init__()



airIndia = airBus()
airIndia.speedVerify()