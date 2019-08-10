class EmployeeDetails:

    total_num_employee = 0

    def __init__(self, name, age, department, pan_no, emp_cd):
        self.emply_name = name
        self.emply_age = age
        self.dept = department
        self.pan_num = pan_no
        self.emply_code = emp_cd
        EmployeeDetails.total_num_employee += 1
    
    def print_employee_details(self):
        print("--- Employee Details ---")
        print("Employee Name is " , self.emply_name)
        print("Employee Code is ", self.emply_code)
        print("Employee Age is ", self.emply_age)
        print("Employee Department is ", self.dept)
        print("Employee pan card number is ", self.pan_num)

if __name__ == "__main__":

    emp_name = input("Enter Employee Name : ")
    emp_age = int(input("Enter Employee age : "))
    emp_dep = input("Enter Employee Department : ")
    emp_pan = input("Enter PAN card no : ")
    emp_code = input("Enter Employee code : ")
    emp_one_obj = EmployeeDetails(emp_name, emp_age, emp_dep,
                                  emp_pan, emp_code)
    emp_two_obj = EmployeeDetails("AAA", 34, "Housekeeping",
                                  "FQWER009", "HSK123")
    emp_one_obj.print_employee_details()
    emp_two_obj.print_employee_details()
    print("No. of employee are " , EmployeeDetails.total_num_employee)