import random
num=random.randint(1,100)
guess=0
attempts=0

while num!=guess:
    guess=int(input("guess the number"))
    attempts +=1
    if guess>num:
        print("guess lower")
    elif guess<num:
        print("guess higher") 
    else:
        print("guessed correctly") 
        print("the number of attempts are:",attempts)      