import math

def geometric_arithmetic_mean_difference():
    a, b = map(int, input().split())
    d = math.sqrt(a*b) - (a+b)/2
    print(f"{d:.2f}")

if __name__ == "__main__":
    geometric_arithmetic_mean_difference()  