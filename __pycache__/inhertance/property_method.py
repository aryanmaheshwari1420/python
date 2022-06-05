class Employee:
    company = "devil juice"
    salary  = 56000
    salarybonus = 500

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

e = Employee()
print(e.totalSalary)        