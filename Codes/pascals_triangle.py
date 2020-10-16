def fill_in(triangle):
    for i in range(len(triangle)):
        triangle[i] = [0] * (i + 1)
        triangle[i][0] = 1
        triangle[i][i] = 1
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

def print_nice(triangle):
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            print(triangle[i][j], end=" ")
        print()

def main():
    triangle = [0] * 11
    fill_in(triangle)
    print_nice(triangle)

main()
