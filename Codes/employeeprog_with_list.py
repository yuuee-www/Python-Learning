from employee_module import Employee    

def main():
    

    selection = 'a'
    employee_list = []
    
    while selection != 'q':
        print("\n\tType: ")
        print("\t\tc - to create an employee")
        print("\t\tv - to view all employees' details")
        print("\t\tq - to quit\n")

        selection = input("\tEnter selection: ")[0]
        if selection == 'c':
            name = input("\n\tEnter the employee's name: ")
            employee = Employee(name)
            employee_list.append(employee)
        elif selection == 'v':
            if len(employee_list) == 0:
                print("There are no employees")
            else:
                print("The employees are: ")
                for employee in employee_list:
                    print("\t", employee)

    print("\tPROGRAM ENDED\n")

if __name__ == "__main__":
    main()

