def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]

                
alist = [1,2,3,4,5,8,7,6]
bubbleSort(alist)
print(alist)
