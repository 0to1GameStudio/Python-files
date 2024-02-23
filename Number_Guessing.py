import random

highest = 10
answer = random.randint(1,highest)
guess = 0
print("Please guess number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())

    if guess == answer:
        print("You got it first time")
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")
   #     guess = int(input())
    #    if guess == answer:
     #       print("Well done, you guessed it")
      #  else:
       #     print("sorry, you have guessed wrong")
