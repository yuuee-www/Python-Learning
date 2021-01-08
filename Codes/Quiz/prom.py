n, m = map(int, input().split())
k = int(input())
l1 = []
l2 = []
for i in range(n):
    l1.append(i+1)
for i in range(m):
    l2.append(i+1)

for i in range(k):
    print(str(l1[i%len(l1)])+' '+str(l2[i%(len(l2))]))