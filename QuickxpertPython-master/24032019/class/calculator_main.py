#import calculator_functions as cf
from calculator_functions import *

if __name__ == "__main__":
    continue_flg = ""
    while continue_flg != "n":
        first_num = input("Enter first number : ")
        second_num = input("Enter second number : ")
        x_num = int(first_num)
        y_num = int(second_num)
        print("Select choices from list ['Add', 'Sub', 'Mul', 'Div']")
        choice = input("Enter your caculator choice : ")
        if choice == "Add":
            print("Additon of %s and %s is %d" % (first_num, second_num, \
                                                    add(x_num, y_num)))
        elif choice == "Sub":
            print("Subtraction of %s and %s is %d" % (first_num, second_num, \
                                                        sub(x_num, y_num)))
        elif choice == "Mul":
            print("Multiple of %s and %s is %d" % (first_num, second_num, \
                                        multiplication(x_num, y_num)))
        elif choice == "Div":
            print("Division of %s and %s is %d" % (first_num, second_num, \
                                                division(x_num, y_num)))
        else:
            print("Invalid choice")
        continue_flg = input("Enter y to continue and n to stop : ")
        