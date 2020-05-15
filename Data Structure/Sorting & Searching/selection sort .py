def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionofMax = 0
        for location in range (1,fillslot + 1):
            if alist[location] > alist[positionofMax]:
                positionofMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionofMax]
        alist[positionofMax] = temp

alist = [1,2,3,4,5,8,7,6]
selectionSort(alist)
print(alist)

'''比对：O(n^2)
   交换：O(n)'''
