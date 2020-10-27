def main():
    sum = 0.0
    with open("bad_numbers.txt") as file:
        for n in file.read().split():
            # try to convert n to a float, but if it
            # is not a valid float, print error message
            try:
                print(float(n))
                sum += float(n)
            except ValueError:
                print("Invalid number:", n)
    print("Sum is:", round(sum, 1))

main()