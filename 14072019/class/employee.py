class Employee:
    def __init__(self, name_val, emplo_cd_val):
        self.name = name_val
        self.cd_val = emplo_cd_val
    
    def get_employee_details(self):
        return "Employee Name is {} and code is {}".format(self.name, self.cd_val)
