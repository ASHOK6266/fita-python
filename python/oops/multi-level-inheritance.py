class ContractorOne():
    def floors(self):
        print("Single floor")


class ContractorTwo(ContractorOne):
    def design(self):
        print(" Duplex design model")

        
 def floors(self):
        print(" Two floor with duplex design model")

class ContractorThree(ContractorTwo):
    
    def entryExit(self):
        print(" Each floor has two entris and exits ")


build1 = ContractorThree()
build1.design()
build1.floors()