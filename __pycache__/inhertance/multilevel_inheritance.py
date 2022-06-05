# multilevel inheritance occurs when the child class inherits from more than one parent class

#in this we have 1 parent class and 2 child class
class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        print("I am an employee so i am luckily breathing...")

class Programmer(Employee):
    company = "fiverr"

    def getsalary(self):
        print("no salary to programmers")

''' yaha par person programmer ka dada hain  aur pogrammer person ka pota hain aur programmer ke pitaji employee hain employee ke beta programmer hain'''


p = Person()
e = Employee()
pr = Programmer()

p.takeBreath()
e.takeBreath()
pr.takeBreath() # as it inherit the property of employee it will print the takebreath method of employee 
