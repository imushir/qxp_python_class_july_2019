class Calculator:
    def __init__(self, first_num, secnd_num):
        self.first_number = first_num
        self.second_number = secnd_num
    
    def addition(self):
        add_val = self.first_number + self.second_number
        return add_val
    
    def subtraction(self):
        sub_val = self.first_number - self.second_number
        return sub_val
    
    def multiplication(self):
        mul_val = self.first_number * self.second_number
        return mul_val
    
    def division(self):
        div_val = self.first_number / self.second_number
        return div_val

if __name__ == "__main__":

    x_num = int(input("Enter first number : "))
    y_num = int(input("Enter second number : "))
    cal_obj = Calculator(x_num, y_num)
    choice = input("Enter Your Choice\n1: Add\n2: Subtraction\n" \
                   "3: Multiplication\n4: Division\n")
    if choice == "1":
        add_reslut = cal_obj.addition()
        print("Addition of %d and %d is %d " %(x_num, y_num, add_reslut))
    elif choice == "2":
        sub_result = cal_obj.subtraction()
        print("Subtraction of {} and {} is {}".format(x_num, y_num, sub_result))
    elif choice == "3":
        mul_result = cal_obj.multiplication()
        print("Multiplication of {} and {} is {}".format(x_num, y_num, mul_result))
    elif choice =="4":
        div_result = cal_obj.division()
        print("Division of {} and {} is {}".format(x_num, y_num, div_result))
    else:
        print("Please Select valid choice")