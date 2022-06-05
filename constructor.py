class Employee:
    company = "Google"
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getdetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the Salary of the employee is {self.salary}")
        print(f"the subunit of the employee is {self.subunit}")
   


Aryan = Employee("Aryan", 5000,"google") 
Aryan.getdetails()       