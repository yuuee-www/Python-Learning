def is_in_binary(lst, val):
    if len(lst) == 0:
        return False
    start = 0
    end = len(lst)
    while end - start > 1:
        middle = (start+end)//2
        if val > lst[middle]:
            start = middle
        else:
            end = middle
    return lst[start] == val

def is_in_binary_recursion(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binarySearch(alist[:mid], item)
            else:
                return binarySearch(alist[mid:],item)
