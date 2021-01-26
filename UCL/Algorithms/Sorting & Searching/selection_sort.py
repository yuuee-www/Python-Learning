#low to high
#-Scan the array from left to right
#-In iteration i, find the index min of the smallest remaining entry in the array
#-swap a[i] and a[min]

def selectionSort(alist):
    for fillslot in range(len(alist)):
        positionofMin = len(alist)-1
        for location in range (fillslot,len(alist)):
            if alist[location] < alist[positionofMin]:
                positionofMin = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionofMin]
        alist[positionofMin] = temp

alist = [1,2,3,4,5,8,7,6]
selectionSort(alist)
print(alist)