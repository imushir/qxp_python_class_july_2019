



if __name__ == "__main__":
    
    first_num = input("Enter first number : ")
    second_num = input("Enter second number : ")
    x_num = int(first_num)
    y_num = int(second_num)
    try:
         div_result = x_num / y_num
         print("Division of {0} and {1} is {2} ".format(first_num, second_num, div_result))
    except ZeroDivisionError as zr_err:
        print("Zero Exception error is", zr_err)
    except Exception as err:
        print("Error is : ", err)
    finally:
        print("Closing the program.")
    