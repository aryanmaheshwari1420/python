import random
randno = random.randint(1,100)
# print(randno)
userguess = None
guesses =0
while(userguess!=randno):
    userguess = int(input("Enter your guess: "))
    guesses+=1
    print("\n")
    if (userguess==randno):
        print("You guessed it right\n")
    else:
        if userguess>randno:
            print("your guessed it wrong!  Enter a smaller number\n")
        else:
            print("your guessed it wrong!  Enter a larger number\n")

print(f"\tYoU guessed the number in {guesses} guesses\n")

with open ("highscore.txt","r") as f:
    highscore = int(f.read())

if (guesses<highscore):
    print("*****you have just broken the high score!*****")
    with open ("highscore.txt","w") as f:
        f.write(str(guesses))    