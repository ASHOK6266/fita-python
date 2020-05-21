import re

class User():

    def __init__(self,email,firstname,lastname,password,age):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.age = age

    def emailValidate(self):
        pattern = "[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu|net)" 
        if(re.search(pattern,self.email)):
            return True
        else:
            return False
        
    
    def firstName(self):
        if self.firstname.isalpha() and self.lastname.isalpha():
            return True
        else:
            print("The firstname and lastname is invalid and should contain only characters")

    def passWord(self):
        if len(self.password) > 8 and len(self.password) < 40:
            return True
        else:
            print(" The password should be betweeen minimum of 8 character lenth and maximum of 40 character")

    def Age(self):
        if self.age > 13:
            return True
        else:
            print(" Age is valid")

    
    def isValid(self):
        if self.emailValidate():
            if self.firstName():
                if self.passWord():
                    if self.Age():
                        print("The user is valid user")
                        return True


userOne = User("ashok@gmail.com","ashok","baskaran","azertyzgvcye",26)
userOne.isValid()
            