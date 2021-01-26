def mergeSort(alist):
    if len(alist)<=1:
        return alist

    middle = len(alist) // 2
    left = mergeSort(alist[:middle])
    right = mergeSort(alist[middle:])

    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged

alist = [1,2,3,4,5,8,7,6]
lst = mergeSort(alist)
print(lst)

