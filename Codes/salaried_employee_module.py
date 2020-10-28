###  This module defines a class that models a salaried employee.
#
from employee_module import Employee

## A salaried employee has a name, a salary and a starting date 
#
class SalariedEmployee(Employee) :
    
    INITIAL_SALARY  = 10000
    INCREMENT = 1000
       
    ## Constructs a SalariedEmployee with a name an annual salary.
    #  @param employee_name the name of the employee.
    #
    def __init__(self, employeeName = "No name", day = 1, month = 1, year = 2000,
                 theSalary = 0):
        super().__init__(employeeName, day, month, year)
        self.salary = theSalary
            
    ##    
    # @return string representation of object.
    #
    def __str__(self):
        return super().__str__() + " salary: " + str(self.salary)

    ## salary property allows get/set access to Employee's salary.
    #  salary will be set to zero if there is an attempt to reduce
    #  it below zero.
    #
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salaryAmount):
        if salaryAmount < SalariedEmployee.INITIAL_SALARY:
            self._salary = SalariedEmployee.INITIAL_SALARY
        else:
            self._salary = salaryAmount
       
    ## Promotes the employee by increasing the salary by INCREMENT.    
    #
    def promote(self):
        self.salary += SalariedEmployee.INCREMENT

    ## Demotes the employee by decreasing the salary by INCREMENT.    
    #
    def demote(self):
        self.salary -= SalariedEmployee.INCREMENT         
         
    ## Raises the salary of the employee by the amount passed as a parameter.    
    # @param pay_rise the amount by which the the salary should be raised.
    #
    def raise_salary_by(self, pay_rise):
        if pay_rise > 0 :
            self.salary += pay_rise
        
    ## Determines if this employee is equal to another employee.
    #  @param rhsValue the right-hand side employee.
    #  @return True if the names and the salaries are equal.
    #  @exception TypeError if the objects being compared are not
    #             the same type.
    #            
    def __eq__(self, rhsValue) :
        if isinstance(rhsValue, SalariedEmployee) :
            return super().__eq__(rhsValue) and self.salary == rhsValue.salary
        elif isinstance(rhsValue, Employee) :
            print("\n>>> Warning, you are comparing a SalariedEmployee with an Employee.")
            return super(SalariedEmployee, self).__eq__(rhsValue)
        else:
            raise TypeError("Argument must be a Salaried Employee object.")


def main() :
    # a simple main function to test this class
    semployee1 = SalariedEmployee("Bart Simpson", 30, 11, 2018, 15035)
    semployee2 = SalariedEmployee("Marge Simpson", 31, 1, 2018, 15035)
    semployee3 = SalariedEmployee()
    employee4 = Employee()

    print("First SalariedEmployee: " + str(semployee1))
    print("Second SalariedEmployee: " + str(semployee2))
    print("Third SalariedEmployee: " + str(semployee3))
    print("Fourth Employee: " + str(employee4))

    if semployee1 != semployee2 :
        print("First Employee and Second Employee are not equal.")
    else:
        print("First Employee and Second Employee are equal.")
    
    if semployee3 != employee4 :    
        print("Third Employee and Fourth Employee are not equal")
    else :
        print("Third Employee and Fourth Employee are equal")
    
if __name__ == '__main__':
    main()                  