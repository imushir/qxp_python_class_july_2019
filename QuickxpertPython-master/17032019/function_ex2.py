def subtraction(a_num, b_num):
    sub = 0
    if a_num > b_num:
        sub = a_num - b_num
    else:
        sub = b_num - a_num
    return  sub

def division(c_num, d_num):

    div = c_num / d_num
    return div

def multiplication(e_num, f_num):
    mul = e_num * f_num
    return mul


if __name__ == "__main__":

    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    sub_result = subtraction(num1, num2)
    div_result = division(num1, num2)
    mul_result = multiplication(num1, num2)
    print("Substraction of %d and %d is %d " % (num1, num2, sub_result))
    print("Division of %d and %d is %d " % (num1, num2, div_result))
    print("Mulplication of %d and %d is %d " % (num1, num2, mul_result))
