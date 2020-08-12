import random
import time

min = 1  # Because the minimun value a die can roll is 1
max = 6  # Because the maximun value a die can roll is 6

roll_again = "yes"  # First condition is True to tart the loop
while roll_again != "no" and roll_again != "n":
            print ("\nRolling the dices...")
            time.sleep(1.5) # give time to roll the dice, a sense of realistic
            dice1=random.randint(min, max)
            dice2=random.randint(min, max)
            print ("The values are....")
            print ("Dice 1 =",dice1)
            print ("Dice 2 =",dice2)
            if dice1 == dice2:  # If two dices are equal 
                print('You win a double!')    
            else:
                print('Keep trying!')
            roll_again = input("Roll the dices again? ['no' or 'n' to quit]\n")
