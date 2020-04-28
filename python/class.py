class user():
    '''

    '''
    def __init__(self,name,age):
        self.name = name  #key example
        self.age = age
        
    def printing(self):
        print("This is name : ", self.name) 
        print("This is the age : ", self.age)

    def agepredict(self):
        if self.age > 18:
            print(" He is major")
        else:
            print(" He is minor")

    def nameCount(self):
        print(" The character length ",len(self.name))

    def allDetails(*self):
        for each in self:
            print(each)

person1 = user(["Ashok",25,"arun",24])
person1.printing()
person1.agepredict()
person1.nameCount()
person1.allDetails()











