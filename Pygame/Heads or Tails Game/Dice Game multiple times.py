import random as m
import statistics as stat
import time

min = 1
max = 6
history = []
def one():
    while True:
        ans = input("Do you want to throw a dice? [Enter 'y' for yes \
                                                    and 'n' for no] \n  ")
        if ans == "Y" or ans == "y":
            roll = m.randint(min,max)
            print(f"You have rolled a {roll}")
            history.append(roll)
            print("So far you have rolled: {}".format(history))
            mean = stat.mean(history)
            print(f"Your mean value is {mean}")
        elif ans == "N" or ans == "n":
            break
        else:
            print("You have entered a wrong symbol!")
    print("You have finished your game!")
    print(f"Your history is {history} \n Your mean number is {mean}")

def more(x):
    while x != 0:
        history.append(m.randint(1,6))
        x -= 1
    mean = stat.mean(history)
    print(f"You have rolled: {history}. \n Your mean value is: {mean}")

which = str(input("Do you want to play manually or let the program\
                                    do this for you? Enter 1 or 2: "))
if which == "1":
    one()
elif which == "2":
    try:
        num = int(input("How many trials do you want me to do?: "))
        if num >= 0:
            more(num)
        else:
            print("You have entered a negative number.")
    except:
        print("Wrong input!")
        print()
