n = int(input())
s = list(map(float, input().strip().split()))
s.sort()
ns = s[1:-1]
print(f"{sum(ns)/(n-2):.2f}")