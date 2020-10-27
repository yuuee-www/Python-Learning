shoppingListFile = open("shopping_list.txt", "r")

line = shoppingListFile.readline()
while line != "":
    line = shoppingListFile.readline().rstrip()
    print(line)
    
shoppingListFile.close()