#from maths_functions import add, print_error_msg
from maths_functions import *

if __name__ == "__main__":

    print_greeting_msg("Good Morning")
    
    print("Select 1--> Add , 2 --> Sub, 3 --> Mul" \
          "4 --> Div 5 --> Area of Circle")
    choice = input("Enter Choice ")
    if choice in ["1", "2", "3", "4"]:
        val_one = int(input("Enter first number : "))
        val_two = int(input("Enter second number : "))
        if choice == "1":
            result_add = add(val_one, val_two)
            print("Addition is ", result_add)
        elif choice == "2":
            result_sub = sub(val_one, val_two)
            print("Substraction is ", result_sub)
        elif choice == "3":
            result_mul = mul(val_one, val_two)
            print("Multiplication is : ", result_mul)
        else:
            result_div = div(val_one, val_two)
            print("Division is : ", result_div)
    elif choice == "5":
        radius = int(input("Enter Circle Radius value : "))
        area_val = area_circle(radius)
        print("Area of circle is ", area_val)
    else:
        print_error_msg()