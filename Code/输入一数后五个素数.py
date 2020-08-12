def prime(m):
    p=1
    for i in range(2,int(pow(m,0.5)+1)):
        if(m%i==0):
            p=0
            break
    return p

n = eval(input())
cnt=1
while(cnt<=5):
    if(prime(int(n))):
        cnt=cnt+1
        if(cnt<6):
            print("{},".format(n))
        else:
            print(n)
    n=n+1
