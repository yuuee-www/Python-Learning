def quickSort(alist):
    if len(alist) <=1:
        return alist
    else:
        pivot = alist[0]
        less_than_pivot = [x for x in alist[1:] if x <= pivot]
        more_than_pivot = [x for x in alist[1:] if x > pivot]
        return quickSort(less_than_pivot) + [pivot] + quickSort(more_than_pivot)

alist = [1,2,3,4,5,8,7,6]
lst = quickSort(alist)
print(lst)