#EXERCISE
"""
Write an object oriented program that performs the following
tasks:
1. Define a class called "Employee" and create an instance
of that class
2. Create an attribute called name and assign it with a
value
3. Change the name you previously defined within a
method and call this method by making use of the object you created
"""

class Employee:
    name = "ak"
    print(name)

    def changeName(self):
        self.name = 'ba'
        print(self.name)

EmployeeOne = Employee()
EmployeeOne.name
EmployeeOne.changeName()