def Odd_or_Even():
    a = input("Please enter an integer:")
    while type(eval(a)) != int:
        print("That's not a valid input.")
        a = input("Please enter an integer:")

    print(f"{a} is {Is_Odd_or_Even(a)}.")    


def Is_Odd_or_Even(a):
    if int(a) % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

if __name__ == "__main__":
    Odd_or_Even()