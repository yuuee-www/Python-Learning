class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def add(self,item):
        self.queue.insert(0, item)

    def pop(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

def xor_seq(lst):
    queue_1 = Queue()
    for item in lst:
        queue_1.add(item)
    
    result_list = [0,]

    while queue_1.size() != 1:
        result = queue_1.pop()^queue_1.pop()
        result_list.append(result)
        queue_1.add(result)

    return sum(result_list)    

def calculate_xor_seq():
    n = int(input())
    lst = input().split(" ")
    lst = [int(lst[i]) for i in range(len(lst))]
    if len(lst) == n:
        print(xor_seq(lst))

if __name__ == "__main__":
    calculate_xor_seq()