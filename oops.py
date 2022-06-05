class Employee:
    company = "Google"

Aryan = Employee()
Dost = Employee() 
print(Aryan.company)
print(Dost.company)   
Employee.company= "Youtube"
print(Aryan.company)
print(Dost.company)