#THE PERFECT GUESS
import random

num=random.randint(1,100)
attempt=1
guess=int(input("Guess the number bud:"))


while(True):
    if guess>num:
        guess=int(input("Guess another number dude.This is big: "))
        attempt+=1
    elif guess<num:
        guess=int(input("Guess another number dude.This is small: "))
        attempt+=1
    else:
        print(f"You guessed it right BUD! You took {attempt} attempts")
        break
