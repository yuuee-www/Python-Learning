def coin_change(cList,change):
    minCoins = change
    if change in cList:     #Remain change is the value in cList
        return 1
    else:
        for i in [c for c in cList if c <= change]:
            numCoins = 1 + coin_change(cList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


print(coin_change([1,4,6],9))
