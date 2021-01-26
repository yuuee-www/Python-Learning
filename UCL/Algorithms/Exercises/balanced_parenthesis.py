from pythonds.basic.stack import Stack

def balanced_parenthesis(s):
    p = Stack()   
    for ch in s:
        if(ch=="("):
            p.push(ch)
        elif(ch==")"):
            p.pop()
    return p.isEmpty()

print(balanced_parenthesis("((x*2)+(x-2)) – a[3] / a[10]"))
print(balanced_parenthesis("(((x*2)+(x-2)) – a[3] / a[10]"))