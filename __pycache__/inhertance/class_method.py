# class method is a method which is bound to the class nd not the object of the class


class Employee:
    company = "google"
    salary = 100
    location = "denmark"

    def changesalary(self,sal):
        self.salary = sal

e = Employee()
print(e.salary)

e.changesalary(520)
print(e.salary)

print(Employee.salary)
print(e.salary)
                     # or




class Employee:
    company = "google"
    salary = 100
    location = "denmark"

    def changesalary(self,sal):
        self.__class_.salary = sal

    @classmethod
    def changesalary(cls,sal):
        cls.salary= sal    

