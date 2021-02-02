def triplicates(arr1, arr2, arr3):
    return sorted(set(arr1) & set(arr2) & set(arr3))

#or use bucket sort