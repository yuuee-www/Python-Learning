def look_up():
    n, m = map(int, input().split())
    dic = {}
    lst = []
    for i in range(n):
        s = input()
        if not dic.__contains__(s):
            dic[s] = 1
        else:
            dic[s] += 1
    for i in range(m):
        s = input()
        if dic.__contains__(s):
            lst.append(dic[s])
        else:
            lst.append("Not Found!")
    print('\n'.join(str(item) for item in lst)) 

if __name__ == "__main__":
    look_up()

    
