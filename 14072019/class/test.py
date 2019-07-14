from employee import Employee


def employ_changed(self):
    print("Department Changed")
    print("New values", 123)


Employee.get_employee_details = employ_changed
emp_obj = Employee("Mushir", 123)
emp_obj.get_employee_details()