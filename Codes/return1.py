import random

def Spin(num):
    if num == 1:
        return 'Good luck boi!'
    elif num == 2:
        return 'Try your luck ocne again!'
    elif num == 3:
        return 'Yes'
    elif num == 4:
        return 'ohhh'
    elif num == 5:
        return 'Very doubtful'

r = random.randint(1,5)
fortune = Spin(r)
print(fortune)
