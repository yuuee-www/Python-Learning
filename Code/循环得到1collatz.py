def collatz(number):
    while True:
        if number == 1:
            return 1
        else:
            if number%2 == 0:
                number = number//2
                print(number)
            elif number%2 == 1:
                number = 3*number + 1
                print(number)
try:
    number = int(input("请输入一个整数->:"))
    collatz(number)
except ValueError:
    print("please input a integer number")
