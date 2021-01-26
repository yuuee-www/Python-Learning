def bucketSort(alist):
    bucket = []
    for i in range(0, max(alist)+1):
        bucket.append(0)

    for i in alist:
        bucket[i] += 1

    lst = []

    for i in range(0, len(bucket)):
        for j in range(1, bucket[i]+1):
            lst.append(i)
    
    return lst

alist = [1,2,3,4,5,8,7,6,6]
lst = bucketSort(alist)
print(lst)