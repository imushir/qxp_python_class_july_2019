class AccountDepartment(object):

    def __init__(self):
        self.company_name = "XYZ"
        self.salary_amount = 20000
    
    def get_pf_deduction(self):
        pf_ammnt = (self.salary_amount * 2) / 100
        return pf_ammnt

class ItDepartment(AccountDepartment):

    def __init__(self, salary_val):
        super(ItDepartment, self).__init__()
        self.it_depart_salary = salary_val

    def get_pf_deduction(self):
        base_class_pf = super(ItDepartment, self).get_pf_deduction()
        print("Base class pf : ", base_class_pf)
        it_pf_amnt = (self.it_depart_salary * 4) / 100
        return it_pf_amnt


if __name__ == "__main__":
    it_depart_obj = ItDepartment(20000)
    pf_val = it_depart_obj.get_pf_deduction()
    print("PF value is : ", pf_val)