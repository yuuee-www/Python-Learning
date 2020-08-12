# Writing to a file
numFile = open ("DATA1.txt", "w")
user = True
while user == True:
    num = eval(input("Number: "))
    if num < 0:
        user = False
    else:
        numFile.write(str(num) + "\n")  #\n forces the input onto another line
        
numFile.close()