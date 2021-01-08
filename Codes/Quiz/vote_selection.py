a = int(input())
dic = {}
while a:
    name = input()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1
    a = a - 1

for key,value in dic.items():
    if value == max(dic.values()):
        print(key)
        print(value)