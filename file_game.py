def game():
    return 446

score = game()
with open("high_score.txt") as f:
    high_score = f.read()

if high_score == '' :
    with open("high_score.txt",'w') as f:
        f.write(str(score))
elif (high_score)<score:
    with open("high_score.txt",'w') as f:
        f.write(str(score))


    
