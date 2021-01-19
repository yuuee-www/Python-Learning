class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

    def __repr__(self):
        return str(self.elem)

class CircularList:
    def __init__(self, node = None):
        self.rear = node
        self.head = node
        if node:
            node.next = node
    
    def is_empty(self):
        return self.rear == None

    def length(self):
        if self.is_empty():
            return 0
        else:
            cur = self.rear
            count = 1
            while cur.next != self.rear:
                count += 1
                cur = cur.next
            return count

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.rear = node
            node.next = node
        else:
            node.next = self.rear.next  
            self.rear.next = node
            self.rear = node
            

    def prepend(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.rear = node
            node.next = node
        else:
            node.next = self.head
            self.head = node
            self.rear.next = node
            
            

    def delete(self, pos):
        if self.is_empty():
            return
        cur = self.head 
        pre = None
        cnt = 1
        while cur.next != self.head:
            if pos == cnt:
                if cur == self.head:   
                    self.head = cur.next
                    self.rear.next = self.head
                else:
                    pre.next = cur.next  
                return
            else:
                pre = cur
                cur = cur.next
                cnt += 1
        
    def printList(self):
        if self.is_empty():
            return
        p = self.rear.next
        print("Head", end=' ')
        while True:
            print("-->", p.elem, end=' ')
            if p is self.rear:
                break
            p = p.next
        print("--> Rear")

