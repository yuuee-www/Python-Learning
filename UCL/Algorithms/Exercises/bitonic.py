def bitonic(arr):
    for i in range(len(arr)-1):
        if arr[i]<=arr[i+1]:
            continue
        elif arr[i]>arr[i+1]:
            break
    #print(i)
    if i == (len(arr)-2):
        return True

    for j in range(i, len(arr)-1):
        if arr[j]>=arr[j+1]:
            continue
        elif arr[j]<arr[j+1]:
            j -= 1
            break
    #print(j)
    if j != (len(arr)-2):
        return False
        
    return True

print(bitonic([2,4,6,8,10,12,11,9,7,5]))
print(bitonic([2,4,6,8,10,12,11,9,7,1,5,3,6]))
print(bitonic([2,4,6,8,10,12,11,9,7,5,3,6]))
print(bitonic([2,4,6,8,10,12]))
print(bitonic([2,4,6,8,10,12,11]))
print(bitonic([2,1,0]))
print(bitonic([1,2,1]))