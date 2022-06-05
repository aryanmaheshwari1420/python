# create a class with a class attribute a ; create an object from it and set a directly using object a = 0 does this change the class attribute?
class sample:
    a = "aryan"

obj = sample() 
obj.a = "vishu"
sample.a="sonu"
print(sample.a)
print(obj.a)
print(sample.a)

# no class attibut does not change