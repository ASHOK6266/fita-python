'''
class Employee:
    def employeeDetails(self):
        self.name = "Ashok kumar BASKARAN"
        print("The name is ",self.name)
        age = 23
        print(" The age is ",age)
    
    def printEmployeeDetails(self):
        print(" The second print method")
        print(" print the age again ",age)

employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()

'''

class Employee:

    def employeeDetails(self):
        self.name = "Ashok"

    @staticmethod
    def welcomeMessage():
        print("Welcome to this organisation")
employeeOne = Employee
employeeOne.welcomeMessage()