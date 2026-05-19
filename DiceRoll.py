import random
num=random.randint(1,6)
attempts=0
guess=0

while num!=guess:
    guess=int(input("enter a number b/w 1-6:"))
    attempts +=1
    if guess!=num:
        print("try again")
    else:
        print("correct guessing!!")
        print("the number of attempts are:",attempts)
        print("the actual number was:",num)   
