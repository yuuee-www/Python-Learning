nlist = a = [int(i) for i in input().split()]

searchItem = int(input('Enter a number to search for: '))

found = False
for i in range(len(nlist)):
    if nlist[i] == searchItem:
        found = True
        print(searchItem, ' was found in the list at index ', i)
        break
if found == False:
    print(searchItem, ' was not found in the list!')
