import random
Num = random.randint(1,20)
print('1~20')

for round in range(1,6):
    print('take a shot')
    gue = int(input())

    if gue < Num:
        print('higher')
    elif gue > Num:
        print('lower')
    else:
        break

if gue == Num:
    print('congrats!'+'in '+str(round))

else:
    print('idiot motherfucker'+'the number is'+str(Num))
