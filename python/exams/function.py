'''
Write a function that takes n number of input and returns the name which has A 1.5


Pass a detailed name, age, from and destination, fare
[sara, 13, muich : frankfurt]-->  [sara, 13,fare, muich : frankfurt]
0-3 = no charge
3-12 = 50 charge
12-15 = 70 charge 
15= full charge
 
'''

def calculateFare(*passengerDetails):
    #print(type(passengerDetails))
    TicketFare = 150
    for detail in passengerDetails:
        if detail[1] < 3:
            result = list(detail)
            TicketFare = 0
            result.insert(2,TicketFare)
            return result
        elif detail[1] > 3 and detail[1] < 12:
            result = list(detail)
            TicketFare = (150*50)/100
            result.insert(2,TicketFare)
            return result
        elif detail[1] > 12 and detail[1] < 15:
            result = list(detail)
            TicketFare = (150*70)/100
            result.insert(2,TicketFare)
            return result
        else:
            result = list(detail)
            result.insert(2,TicketFare)
            return result
pass1 = ['papa',2,'Munich','Frankfort']
pass2 = ['Max',5,'Munich','Frankfort']
pass3 = ['sara',14,'Munich','Frankfort']
pass4 = ['Clara',21,'Munich','Frankfort']

print(calculateFare(pass1))
print(calculateFare(pass2))
print(calculateFare(pass3))
print(calculateFare(pass4))




'''

def testFunction(*paras):
    print(paras[0])
testFunction(['sara',18,'M','f'])

'''

'''
12 cards , random split -> sequence number exits 
	Random in built method, sort

'''








'''
Call rate calculate.
Time in built function 
	Import data 
SR==DR → 0.10
SC == EC ---> but SR ! == DR → .50
SC != EC → 1
[time,startRegion: DestRegion,StartCountry: Endcountry]

'''

