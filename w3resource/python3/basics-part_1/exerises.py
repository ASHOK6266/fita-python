'''
2. Write a Python program to get the Python version you are using.



import sys
print(sys.version)

----------------------------------------------------------------------------------------------------------------------------------------------------------

4. Write a Python program which accepts the radius of a circle from the user and compute the area.



r = float(input(" Kindly enter the radius of the circle "))
result = 3.14 * r * r
print(result)

-------------------------------------------------------------------------------------------------------------------------------------------------------------


5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
Go to the editor


x = input(" Enter your first name ")
y = input(" Enter your last name ")
print("Hallo " +y + " "+ x)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 

'''

in_value = input(" Enter some comma separated value ")
l = in_value.split(",")
t = tuple(l)
print("List : ",l)
print("Tuple : ",t)