class Employee:
    company_name_one = "ABC Solution"
    company_name_two = "Sigma Solution"

    def __init__(self, name, DOJ, Salary, Department):
        self.Employee_name = name
        self.Employee_DOJ = DOJ
        self.Employee_Salary = Salary
        self.Employee_Department = Department

    def get_Employee_details(self):
        print("Employee name: {}\nEmployee DOJ: {}\nEmployee Salary: {}\n" \
              "Employee department: {}".format(self.Employee_name, self.Employee_DOJ, \
                                     self.Employee_Salary, self.Employee_Department))
    
if __name__ == "__main__":
    print("Company name :", Employee.company_name_one)
    employee_obj_one = Employee("Soma Reddy", "3/5/1994", "15000", "Devolper")
    employee_obj_two = Employee("Ram Singh", "2/6/199", "25000", "Senior Devolper")
    employee_obj_one.get_Employee_details()
    print("Company name :", Employee.company_name_two)
    employee_obj_two.get_Employee_details()
