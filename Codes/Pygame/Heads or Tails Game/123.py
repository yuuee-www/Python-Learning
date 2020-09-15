import time
import
guess=0
score = 0  # To record the score of each game
toss = 0  # Variable to store the result of the toss
name = input("Whats your name?\n") # Ask for names of the player
ans_main = input(f"{name}, Do you want to make a try (10 times)? \n[Enter 'y' for yes and 'n' for no] \n") # Ask do they want to play
if ans_main == "Y" or ans_main == "y":
      for i in range(10):
          guess = int(input("Your guess? [Enter '1' for head and '2' for tail]\n"))
          time.sleep(1)  # Make the game more realistic (time to flip the coin)
          toss=random.randint(1,2)
          if toss == guess == 1 or toss==guess == 2:
              print(f"You are right! Your current score is:{score}" )
              score += 1
          else:
              print("Sorry! You are wrong! Your current score is:{score}") # To tell the player the current score
      print(f"Your final score is:{score}")
result=str(score)  # Transfer int into string to write
with open('result.txt','a') as file_handle:  # Record the file of results
      file_handle.write(name+' '+result)     # Write the result
      file_handle.write('\n')  # don't need to close
print()
n=input()
