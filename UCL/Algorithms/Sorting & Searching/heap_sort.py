from binary_heap import*

def heapSort(alist):
    bh = BinHeap()
    bh.buildHeap(alist)
    lst = []
    while not bh.isEmpty():
        lst.append(bh.delMin()) 
    return lst

alist = [1,2,3,4,5,8,7,6,6]
print(heapSort(alist))
