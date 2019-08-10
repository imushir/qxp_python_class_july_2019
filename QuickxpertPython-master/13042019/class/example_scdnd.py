class Employee:
    """
    This Employee class

    """
    company_name = "Quickxpert"      # class variable

    def __init__(self):
        """
        This is constructor of class Employee.
        Initializes the attribute values.

        :returns: None
        :rtype: None
        :author: Qxpert

        """
        # Instance variables
        self.employee_name = ""                  
        self.employee_age = ""
        self.employee_dob = ""
        self.employee_department = ""

    def set_employee_details(self, emply_nm, emply_age, emply_dob, emply_dprt):
        """
        This function will set the employee details.

        :param emply_nm: contains the employee's name
        :type emply_nm: string
        :param emply_age: contains the employee's age
        :type: string
        :param emply_dob: contains the employee's dob
        :type: string
        :param emply_dprt: contains the employee's dprt
        :type: string
        :returns: None
        :rtype: None
        :author: Qxprt

        """
        self.employee_name = emply_nm
        self.employee_age = emply_age
        self.employee_dob = emply_dob
        self.employee_department = emply_dprt

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

   name = input("Enter employee name : ")
   age = input("Enter employee age : ")
   dob = input("Enter employee dob : ")
   department = input("Enter the employee department : ")
   emply_one_obj = Employee()
   emply_two_obj= Employee()
   emply_thr_obj = Employee()
   emply_one_obj.set_employee_details(name, age, dob, department)
   emply_one_obj.get_employee_details()
  