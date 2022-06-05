class Employee:
    company = "Google"
    def getsalary(self,signature):
        print(f"salary for the employee working in {self.company} is {self.salary}\n {signature}")

        @staticmethod
        def greet():
            print("Good Morning, Sir")

        @staticmethod
        def time():
            print("9am in the morning")


Aryan = Employee() 
Aryan.salary = 30000
Aryan.getsalary("thanks")           


Aryan.greet() 
Aryan.time()       