'''
1.
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
2.
12 cards , random split -> sequence number exits 
	Random in built method, sort

'''








'''
3.Call rate calculate.
Time in built function 
	Import data 
SR==DR → 0.10 per minute
SC == EC ---> but SR ! == DR → .50
SC != EC → 1
[time,startRegion: DestRegion,StartCountry: Endcountry]


def callRateCal(**calldetails):
    for key, value in calldetails.items():
        print(" {} is {}",format(key,value))



callRateCal(time=10,startRegion = "tamilnadu",DestRegion = "tamilnadu",StartCountry= "india",Endcountry= "india")


Exercise Question 2: 
Write a function func1() such that it can accept a variable 
length of  argument and print all arguments value
'''

def func1(*args):
    for arg in args:
        print(arg)


func1(20, 40, 60)
func1(80, 100)

'''

Exercise Question 3: 
Write a function calculation() such that it can accept two variables and calculate 
the addition and subtraction of it. And also it must return both addition and subtraction
in a single return call
'''

def calculation(num1,num2):
    sum = num1 + num2
    sub = num1 - num2
    return sum,sub

res = calculation(40, 10)
print(res)



'''
Exercise Question 4: 
Create a function showEmployee() in such a way that it should accept employee name, and 
it’s salary and display both, and if the salary is missing in function call it should show
it as 9000
'''

def showEmployee(name,salary=9000):
    print(" Employee ", name , "salary is :",salary)



showEmployee("Ben", 15000)
showEmployee("Ben")

'''

Exercise Question 5: Create an inner function to calculate the 
addition in the following way

Create an outer function that will accept two parameters a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it

'''


def outerFunc(a,b):
    def innerFunc():
        sum = a+b
        return sum

print(outerFunc(5,5))











































