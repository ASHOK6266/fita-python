class Cars():
    
    def color(self):
        return "G§enerally the color is white"

    def wheels(self):
        return " It is two wheel drive"


class Mahindra(Cars):

    def __init__(self,name):
        self.name = name


    def wheels(self):
        if self.name == 'scorpio':
            return " It is a four wheel drive"
        else:
            return Cars.wheels(self) #1 consumes memory and time 
            return " It is a two wheel drive" #2

scorpio = Mahindra("Thar")
print(scorpio.color())
print(scorpio.wheels())