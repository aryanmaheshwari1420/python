#create class  C2-D vector and use it to create another class representing a 3-D vector
class C2dVec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dvec(C2dVec):
    def __init_(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVec(1,3)
v3d = C3dvec(1,9,10)
print(v2d)
print(v3d)


