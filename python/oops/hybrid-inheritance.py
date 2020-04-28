class boeing():
    def category(self):
        return "passenger & cargo"
    def model(self):
        return "747, 737-max currently available"



class airBus():
    def category(self):
        return "only passerger carriers available"
    def model(self):
        return "A380 is available" 



class quantasAirlines(boeing,airBus):
    def fares(self):
        return "costlier"

class AirFrance(quantasAirlines,boeing):
    def category(self):
        return " cheaper"


'''

ticket1 = quantasAirlines()
print(ticket1.category())
print(ticket1.model())
print(ticket1.fares())

'''

ticket2 = AirFrance()
print(ticket2.category())
print(ticket2.model())
print(ticket2.fares())