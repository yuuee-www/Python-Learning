class Fib():
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        return self.a

fib = Fib();
for i in fib:
    if i > 10:
        break
    print(i)
