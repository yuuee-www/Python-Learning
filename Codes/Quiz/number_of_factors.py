def numberOfFactors(num):
    ans = 1
    x = 2
    while x * x <= num:
        cnt = 1
        while num % x == 0:
            cnt += 1
            num /= x
        ans = cnt
        x += 1
    return ans * (1 + (num > 1))

n = int(input())
print(numberOfFactors(n))

