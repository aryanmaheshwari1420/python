# Multiple inheritance occurs when the child class inherits from more
#than one parent class

#in this we have 2 parent class and one child class

class Employee:
    company = "visa"
    ecode = 120

class FreeLancer:
    company = "fiverr" 
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1
class Programmer(Employee,FreeLancer):
    name = "rohit"

p = Programmer()   
p.upgradeLevel() 
print(p.level)

print(p.company) # as employee come first in inheritance in the programmer class so it will print visa 
