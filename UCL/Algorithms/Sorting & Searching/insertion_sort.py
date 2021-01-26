#low to high
#-Scan the array from left to right
#-In each iteration i, swap a[i] with each larger entry to its left

def insertionSort(alist):
    for index in range(1,len(alist)):
        currentValue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentValue:
            alist[position]=alist[position-1]
            position -= 1
        alist[position]=currentValue

alist = [1,2,3,4,5,8,7,6]
insertionSort(alist)
print(alist)