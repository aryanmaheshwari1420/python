
import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp =='s':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp =='w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp =='g':
        if you == 's':
            return False
        elif you == 'W':
            return True


print("Computer Turn: sanke(s) water(w) or gun(g)?")
rand_no = random.randint(1,3)
if rand_no == 1 :
    comp = 's'
elif rand_no == 2:
    comp = 'w'
elif rand_no == 3:
    comp  = 'g'    

you = input("your turn: sanke(s) water(w) or gun(g)?")  
a = gamewin(comp,you) 

print(f"computer choose {comp}")
print(f"you choose {you}")


if a == None:
    print("the game is a tie")
elif a:
    print("you win!")
else:
    print("you lose!")    
