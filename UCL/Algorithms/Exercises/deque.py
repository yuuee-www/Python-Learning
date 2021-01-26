class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFirst(self, item):
        self.items.append(item)

    def addLast(self, item):
        self.items.insert(0,item)

    def removeFirst(self):
        return self.items.pop()

    def removeLast(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)