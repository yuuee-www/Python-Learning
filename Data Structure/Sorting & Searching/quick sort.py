def quickSort(alist):
    quicksorthelper(alist,0,len(alist)-1)


def quicksorthelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quicksorthelper(alist,first,splitpoint-1)
        quicksorthelper(alist,splitpoint+1,last)



def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

alist=[54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

'''分裂：O(logn)
   归并：O(n)
   总：O(nlogn)
   若中值选取不当，退化到O(n^2)'''
