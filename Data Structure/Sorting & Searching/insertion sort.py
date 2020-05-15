def insertionSort(alist):
    for index in range(1,len(alist)):
        currentValue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentValue:
            alist[position]=alist[position-1]
            position -= 1
        alist[position]=currentValue

lst=[1,2,3,4,5,7,6,8]
insertionSort(lst)
print(lst)

'''O(n^2)'''
