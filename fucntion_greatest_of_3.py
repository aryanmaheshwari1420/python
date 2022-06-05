def greatest_of_three(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
             return c
    else:
        if b>a:
            if b>c:
                return b
            else:
                return c       


    
print("the greatest is " +str(greatest_of_three(10,15,9)))

