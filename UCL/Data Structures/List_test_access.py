import time

aList = []
for length in range(4000, 1000001,10000):
    while len(aList) < length:
        aList.append(42)
    count = 0
    x = 0
    starttime = time.time()

    while count < 1000:
        x += aList[count] #read from beginning
        #x += aList[length//2 + count] #from middle
        # x += aList[length - count - 1] # from end
        count += 1

    now = time.time()
    print(length, now - starttime)
