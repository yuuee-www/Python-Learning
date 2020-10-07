import random

def Pi():
    k = 0
    N = 2**25
    for i in range(N):
        x, y = random.random(), random.random()
        d = pow(x**2 + y**2, 1/2)

        if d < 1.00:
            k += 1
        
        pi = 4 * k / N

    print(f"Pi is approximately {pi}.")

if __name__ == "__main__":
    Pi()