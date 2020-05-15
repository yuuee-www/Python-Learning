alist1=[1,2,3,4,5,6,8,7]
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startpos in range(sublistcount):
            gapInsertionSort(alist,startpos,sublistcount)
        print("After increments of size ",sublistcount,"The list is",alist)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=currentvalue

shellSort(alist1)

'''O(n^3/2)'''
