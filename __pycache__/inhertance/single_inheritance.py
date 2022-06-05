class Employee:
    company = "Google"

    def showDetails(self):
        print("this is an employee")

class Programmer(Employee):
    language = "python"

    def getLanguage(self):
        print(f"the language is {self.language}")

    def showDetails(self):
        print("this is an employee of the google")    

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company) 
p.showDetails()               