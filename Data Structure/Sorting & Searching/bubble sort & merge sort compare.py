import random, timeit
#import the relevant library
from sorting_techniques import pysort

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]

#min/max possible values to generate
min_value = 0 
max_value = 50000

#create a sorting object
sortingObj = pysort.Sorting()

#set how many numbers to generate 
MAXNUMBER = 20000

#create a new random list of integers as above
randomListOfIntegers = [random.randint(min_value, max_value) for i in range(MAXNUMBER)]

#sort the new list using MergeSort
print("Sorting with MergeSort. First 100 elements in the list:")
for i in range(0,99):
    print(randomListOfIntegers[i], end=" ")

sortedList = sortingObj.mergeSort(randomListOfIntegers)

print("\n \nSorting complete. First 100 elements:")
for i in range(0,99):
    print(sortedList[i], end=" ")




#create a new random list of integers 
randomListOfIntegers = [random.randint(min_value, max_value) for i in range(MAXNUMBER)]

#sort it with BubbleSort, compute how long it takes, and print it

starttime = timeit.default_timer()
bubbleSort(randomListOfIntegers)
endtime = timeit.default_timer()
print("BubbleSort took", endtime-starttime, "to sort", MAXNUMBER, "integer numbers")




randomListOfIntegers = [random.randint(min_value, max_value) for i in range(MAXNUMBER)]

#sort it with MergeSort, compute how long it takes, and print it

starttime = timeit.default_timer()
sortingObj.mergeSort(randomListOfIntegers)
endtime = timeit.default_timer()
print("MergeSort took", endtime-starttime, "to sort", MAXNUMBER, "integer numbers")



                
