# Reading from a file
numFile = open("file1.txt", "r")
nameList = []
numList = []
while True:
    text = numFile.readline()

    #把名字存成list
    space = text.find(" ")
    name1 = text[0:space]
    nameList.append(name1)
    num1 = text[space+1:-1]
    numList.append(num1)
            
    if text=="": 
        break
while True:
    userInput = input("Name/ Phone Number: ")
    if userInput in nameList:
        spot = nameList.index(userInput)
        print (numList[spot])
    if userInput in numList:
        spot = numList.index(userInput)
        print (nameList[spot])
    if userInput == "QUIT":
        break


    
numFile.close()
