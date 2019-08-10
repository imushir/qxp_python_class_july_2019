class Employee:
    """
    This Employee class

    """
    company_name = "Quickxpert"      # class variable

    def __init__(self, name, age, date_of_birth, department):
        """
        This is constructor of class Employee.
        Initializes the attribute values.

        :param name: contains the employee's name
        :type name: string
        :param age: contains the employee's age
        :type age: string
        :param date_of_birth: contains the employee's DOB
        :type date_of_birth: string
        :param department: contains the department name
        :type department: string
        :returns: None
        :rtype: None
        :author: Qxpert

        """
        # Instance variables
        self.employee_name = name                  
        self.employee_age = age
        self.employee_dob = date_of_birth
        self.employee_department = department

    def get_employee_details(self):
        """
        This function will print the employee details

        :returns: employee details
        :rtype: string
        :author: Qxprt

        """
        print("Employee Name {}\nEmployee Age {}\nEmployee Date of Birth {}\n" \
              "Employee Department {}".format(self.employee_name, self.employee_age, \
                                       self.employee_dob, self.employee_department))


if __name__ == "__main__":

    print("Company Name:", Employee.company_name)
    employee_obj_one = Employee("AAAA", "23", "10/11/2000", "Accounts" )
    employee_obj_secnd = Employee("BBBB", "24", "09/12/1998", "IT" )
    employee_obj_one.get_employee_details()
    employee_obj_secnd.get_employee_details()
