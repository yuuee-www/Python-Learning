def rearrange(arr):
    arr.sort(key = lambda x:(x<0, abs(x)))  #Positive at the head and neagtive at the tail
    lst = []
    while arr:
        lst.append(arr.pop(0))
        if arr:
            lst.append(arr.pop())
    return lst

alist = [-8, 1, 2, -4, 6, 12, 5, -10, 16, 7, 11]
lst = rearrange(alist)
print(lst)
        