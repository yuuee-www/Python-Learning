###  This module defines a class that models an employee.
#

from employee_module import Employee

## An employee has a name and a salary. 
#
class HourlyEmployee(Employee):

    INITIAL_HOURLY_RATE = 10.0     
    
     ## Constructs a SalariedEmployee with a name an annual salary.
    #  @param employee_name the name of the employee.
    #
    def __init__(self, employeeName = "No name", day = 1, month = 1, year = 2000, theHourlyRate = 0, theHoursPerWeek = 0):
        super().__init__(employeeName, day, month, year)
        self.hourlyRate = theHourlyRate
        self.hoursPerWeek = theHoursPerWeek
            
    ##    
    # @return string representation of object.
    #
    def __str__(self):
        return super().__str__() + " hours per week: " + str(self.hoursPerWeek) \
                + " hourly rate: " + str(self.hourlyRate)

    ## hoursPerWeek property allows get/set access to HourlyEmployee's hours per week.
    #  hoursPerWeek will be set to 0 if there is an attempt to reduce it below zero.
    #
    @property
    def hoursPerWeek(self):
        return self._hoursPerWeek

    @hoursPerWeek.setter
    def hoursPerWeek(self, weeklyHours):
        if weeklyHours < HourlyEmployee.INITIAL_HOURLY_RATE:
            self._hoursPerWeek = HourlyEmployee.INITIAL_HOURLY_RATE
        else:
            self._hoursPerWeek = weeklyHours

    ## hourlyRate property allows get/set access to Employee's hourly rate of pay.
    #  hourlyRate will be set to a base rate if there is an attempt to reduce
    #  it below the base rate.
    #
    @property
    def hourlyRate(self):
        return self._hourlyRate

    @hourlyRate.setter
    def hourlyRate(self, hourlyRateAmount):
        if hourlyRateAmount < HourlyEmployee.INITIAL_HOURLY_RATE:
            self._hourlyRate = HourlyEmployee.INITIAL_HOURLY_RATE
        else:
            self._hourlyRate = hourlyRateAmount
                        
    ## Determines if this hourly paid employee is equal to another hourly paid employee.
    #  @param rhsValue the right-hand side employee.
    #  @return True if the names, hours worked per week and rate of pay are equal.
    #  @exception TypeError if the objects being compared are not
    #             the same type.
    #            
    def __eq__(self, rhsValue) :
        if isinstance(rhsValue, HourlyEmployee) :
            return super().__eq__(rhsValue) \
            and self.hourlyRate == rhsValue.hourlyRate \
            and self.hoursPerWeek == rhsValue.hoursPerWeek
        elif isinstance(rhsValue, Employee) :
            print("\n>>> Warning, you are comparing an HourlyEmployee with an Employee.")
            return super(HourlyEmployee, self).__eq__(rhsValue)
        else:
            raise TypeError("Argument must be an Hourly Employee object.")


def main() :
    # a simple main function to test this class
    hemployee1 = HourlyEmployee("Bart Simpson", 30, 11, 2018, 22.0, 15)
    hemployee2 = HourlyEmployee("Marge Simpson", 31, 1, 2018, 20.0, 10)
    hemployee3 = HourlyEmployee()
    employee4 = Employee()

    print("First HourlyEmployee: " + str(hemployee1))
    print("Second HourlyEmployee: " + str(hemployee2))
    print("Third HourlyEmployee: " + str(hemployee3))
    print("Fourth Employee: " + str(employee4))

    if hemployee1 != hemployee2 :
        print("First Employee and Second Employee are not equal.")
    else:
        print("First Employee and Second Employee are equal.")
    
    if hemployee3 != employee4 :    
        print("Third Employee and Fourth Employee are not equal")
    else :
        print("Third Employee and Fourth Employee are equal")
    
if __name__ == '__main__':
    main()                  