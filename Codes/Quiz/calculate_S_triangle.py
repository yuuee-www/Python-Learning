import math

def heron_formula():
    a, b, c = map(float, input().split())
    p = (a + b + c) / 2
    S = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print(f"{S:.2f}")

def calculate_S_triangle():
    n = int(input())
    for i in range(n):
        heron_formula()
  
if __name__ == "__main__":
    calculate_S_triangle()


#OJ
import math

def heron_formula():
    a, b, c = map(float, input().split())
    p = (a + b + c) / 2
    S = math.sqrt(p*(p - a)*(p - b)*(p - c))
    return S

def calculate_S_triangle():
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(heron_formula())
    
    for s in lst:
        print(f"{s:.2f}")
  
if __name__ == "__main__":
    calculate_S_triangle()