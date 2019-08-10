class MethodOverloadingDemo(object):
    def get_add(self, a_num, b_num):
        add_result = a_num + b_num
        return add_result
    
    def get_add(self, c_num, d_num, e_num):
        add_result_nw = c_num + d_num + e_num
        return add_result_nw
    
if __name__ == "__main__":
    obj = MethodOverloadingDemo()
    addition = obj.get_add(10, 20, 30)
    print("Addition is ", addition)