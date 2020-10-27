with open("shopping_list.txt", "r") as file:
    lineCount = 0
    for line in file:
        print("next line:", line.rstrip())
        lineCount += 1
    print("Line count:", lineCount)

file.close()