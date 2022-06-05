class Employee:
    company = "Google"
    salary = 100

aryan = Employee()
vishu = Employee()

# creating the instance attribute salary for both the objects
aryan.salary = 500 
vishu.salary = 200 # ye ek object ke instances hain  isliye yaha 500 and 200 print karega  # you can analog this with local and global variable
print(aryan.salary)
print(vishu.salary)

#output show  = 500 and 200


# creating the instance attribute salary for both the objects
#aryan.salary = 500 
#vishu.salary = 200
print(aryan.salary)
print(vishu.salary)

#output show = 100 # because it is class instance  yaha hamne class ke andar salary ko  define kiya hain isliye ye 100 print karega


print(aryan.address) # it throws an error as address is not present in class/instance