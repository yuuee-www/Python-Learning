#Unsorted Input: [3,2,4,1]
#Sorted Output: [1,2,3,4]
#Algorithm Output: [4,2,4,3]  indices where flips where performed (4 flips total)

#We have performed 4 flips (bold indicates it has been flipped):
#Start:            [3, 2, 4, 1]
#1st flip (k = 4): [1, 4, 2, 3]
#2nd flip (k = 2): [4, 1, 2, 3]
#3rd flip (k = 4): [3, 2, 1, 4]
#4th flip (k = 3): [1, 2, 3, 4]

def pancakeSort(alist):
    ret = []
    n = len(alist)
    for m in range(n, 0, -1):
        i = alist.index(m)
        if i==m-1:
            alist.pop()
            continue
        elif i==0:
            ret += [m]   
        else:
            ret += [i+1, m]  # Same as ret.extend([i+1, m])
        alist = alist[m-1:i:-1]+alist[:i]
    return ret

print(pancakeSort([3,2,4,1]))
