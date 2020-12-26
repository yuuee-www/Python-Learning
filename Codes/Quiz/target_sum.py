def targetsum(lst, n):
    x = n
    nlst = []
    cnt = len(lst)-1
    i = cnt
    while i >= 0:
        if i == 0 and (x-lst[i]) != 0:
            cnt -= 1
            i = cnt
            nlst = []
            x = n
        elif lst[i] > x :
            i -= 1
            continue
        elif lst[i] < x:
            x = x - lst[i]
            nlst.append(lst[i])
            i -= 1
        else:
            nlst.append(lst[i])
            break   
    nlst.sort()
    print(nlst)
                     

targetsum([1,2,3],6)
targetsum([1,2,3],5)
targetsum([1,4,5,8,12,16,17,20],23)