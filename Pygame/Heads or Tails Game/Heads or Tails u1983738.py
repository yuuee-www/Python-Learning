'''Ce Cao Game Studio Represents'''

import os
import random as m
import statistics as stat
import time
import random as r


def clear():
  os.system('cls')   # Instruction to clear screen for better user experience

def menu():       # User Interface of the main menu of game
  clear()
  print("|",'*'*37,"|")
  print("|","HEAD OR TAILS?".center(37),"|")
  print("|"," ".center(37),"|")
  print("|","- 1.Start -".center(37),"|")
  print("|","- 2.Rules -".center(37),"|")
  print("|","- 3.Result-".center(37),"|")
  print("|","- 4.Quit  - ".center(37),"|")
  print("|"," ".center(37),"|")
  print("|",'*'*37,"|\n")
  
def rule():   # To introduce the rule of the game
  clear()
  print("Rules of the game:")
  print('  Guess Head or Tails for 10 times, if you match the computer guess then you get a point!\"')
  print()

def maingame(): # A block of code which is the main body of the game.  
  clear()
  guess=0
  n = 10 # counter
  score = 0  # To record the score of each game
  toss = 0  # Variable to store the result of the toss
  name = input("Whats your name?\n") # Ask for names of the player
  ans_main = input(f"{name}, Do you want to make a try (10 times)? \n[Enter 'y' for yes and 'n' for no] \n")
  if ans_main == "Y" or ans_main == "y":
      while n>0:
          guess = input("Your guess? [Enter '1' for head and '2' for tail]\n")
          #time.sleep(1)  # Make the game more realistic (time to flip the coin)
          toss=r.randint(1,2)
          if str(toss) == guess:
              score += 1
              print(f"You are right! Your current score is:{score}" )
              print(f"You have {n-1} times to go.")
          elif guess == 'e' and score>=3: # Input e to spend 3 points and roll 5 more times
              score -= 3
              n += 6 # because n-- fter this time of loop
          elif guess != 'e' and guess != '1' and guess != '2':
            print("wrong")
            n+=1
          else:
              print(f"Sorry! You are wrong! Your current score is:{score}") # To tell the player the current score
              print(f"You have {n-1} times to go.")
          n -= 1
  print(f"Your final score is:{score}")
  result=str(score)  # Transfer int into string to write
  with open('result.txt','a') as file_handle:  # Record the file of results
      file_handle.write(name+' '+result)     # Write the result
      file_handle.write('\n')  # don't need to close
  print()

def check(): # Code for checking the results
  ans_check = input('Do you want to print the result in dorder they were played or sorted? \n \
                               [Enter "o" for in order and "s" for sorted]\n')
  if ans_check == 'o':
    clear()
    f = open('result.txt','r') # Another way to operate file I/O
    for line in open('result.txt'):
        line = line.strip() # To make the out put more clear 
        print(line)  # Print the whole file in order
    f.close()  # Remember to close file
  if ans_check == 's':
    clear()
    f = open('result.txt','r')
    result = []    # Read lines and store it as a list
    for line in open('result.txt'): 
        line = line.strip()    
        result.append(line)
    result.sort()   # Sorted 
    for item in result:
      print(item)
    f.close()  


  

num = 0   # Assign initial values to the variable of input(options)
menu()

while num != 4: # 4 is the option to quit
  
  try:
        num=int(input("Please input: "))
        if num == 1: # If the user wants to start a new game
          maingame()
          print("Do you want to restart? \n[1 - restart 2 - check rules 3 - check records 4 - quit]\n" )
                 # Ask the user if he/she wants to play again
        elif num == 2: # If the user wants to check the rule
          rule()
          print("Press Enter to continue...")
          a = input('') # Or we can use os.system("pause") to have similar efect as getchar() in C
          menu()
         
        elif num == 3: # If the user wants to check the results
          clear()
          check()
          print("Press Enter to continue...")
          a = input('') 
          menu()

        elif num == 4: # If the user wants to quit
          clear()
          print("Thanks for playing!") 
          break
        
        else: # If the player input a number other than 1, 2, 3 or 4
          print("\nYou have not entered a correct integer.\n")
          

  except:  # If the plaer enter other wrong input
        print("\nYou have not entered an integer.\n")
        
