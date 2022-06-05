class Employee:
    company = "Google"
    def getsalary(self):
        print(f"salary for the employee working in {self.company} is {self.salary}")

Aryan = Employee() 
Aryan.salary = 30000
Aryan.getsalary()       #Employee.getSalary(Aryan)