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
    #print(passengerDetails)
    TicketFare = 100
    for detail in passengerDetails:
        if detail[1] < 3:
            print("No fare charges")
        elif detail[1] > 3 and detail[1] < 12:
            print(" Chraging 50 percentage")
        elif detail[1] > 12 and detail[1] < 15:
            print(" Charging 70 percentage ")
        else:
            print(TicketFare)


calculateFare(['sara',16,'Munich','Frankfort'])



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

