class BinHeap:
    def __init__(self):
        self.heapList = [0] # Root starts from 1
        self.currentSize = 0

    def percUp(self,i):
        while i//2 >0:
            if self.heapList[i] < self.heapList[i//2]: #From low to high
                tmp = self.heapList[i//2] # Swap with root
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i=i//2 # Move up

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize) # New key goes upwards

    def minChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1  # Return position of minimal child

    def percDown(self,i):
        while i*2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        return self.currentSize == 0

    def buildHeap(self,alist):
        i = len(alist)//2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        #print(len(self.heapList)-1)
        while (i>0):
            #print(self.heapList[1:])
            self.percDown(i)
            i=i-1
        #print(self.heapList[1:])
