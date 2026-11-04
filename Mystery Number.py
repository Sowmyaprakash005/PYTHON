import random
num=random.randint(1,100)
attempts=0
print("Guess a number between 1 and 100")
while True:
    guess=int(input("Guess a number:"))
    attempts+=1
    if guess<num:
        print("Too small! Try again.")
    elif guess>num:
        print("Too large! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
