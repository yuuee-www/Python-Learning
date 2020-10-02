def main():
    first_number = int(input("\n\tEnter the number of the first times table you want: "))


    last_number = int(input("\tEnter the number of the last times table you want: "))

    total_lines = int(input("\tEnter the number of lines for each table: "))

    for table_number in range(first_number, last_number + 1):
        print("")

        for line_number in range(1, total_lines + 1):
            print("\t\t{} x {} = {} ".format(table_number, line_number, (table_number * line_number)))


if __name__ == "__main__":
    main()
