# Super method is used to access the methods of a super class in the desired class
#syntax = super().__init__()

# multilevel inheritance occurs when the child class inherits from more than one parent class

#in this we have 1 parent class and 2 child class
class Person:
    country = "India"

    def __init__(self):
        print("Initializing person...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Initializing employeee...\n")
        

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        print("I am an employee so i am luckily breathing...")

class Programmer(Employee):
    company = "fiverr"

    def getsalary(self):
        print("no salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am an employee so i am luckily breathing...")
    

''' yaha par person programmer ka dada hain  aur pogrammer person ka pota hain aur programmer ke pitaji employee hain employee ke beta programmer hain'''


e =Employee()
e.takeBreath()