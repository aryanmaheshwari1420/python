#create the class programmer for storing information of few programmer working at microsoft
class Programmer:
    company = "Microsoft"
    def __init__ (self,name,product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"the name of then programmer is {self.name} and the product of the programmer is {self.product}")


aryan = Programmer("aryan", "skyopp")
vishu = Programmer("alka","github")
aryan.getInfo()
vishu.getInfo()