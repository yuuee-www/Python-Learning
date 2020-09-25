import random
import time

min = 1
max = 6

roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print ("\nRolling the dices...")
    time.sleep(1.5)
    dice1=random.randint(min, max)
    dice2=random.randint(min, max)
    print ("The values are....")
    print ("Dice 1 =",dice1)
    print ("Dice 2 =",dice2)
    if dice1 == dice2:
        print('You win a double!')
    else:
        print('Keep trying!')
    roll_again = input("Roll the dices again?\n")
