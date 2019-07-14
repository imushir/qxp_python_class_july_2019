def add(a_num, b_num):
    return a_num + b_num

def sub(c_num, d_num):
    return c_num - d_num

def mul(e_num, f_num):
    return e_num * f_num

def div(frst_num, scnd_num):
    return frst_num / scnd_num

def area_circle(radius):
    return 3.14 * radius * radius

def print_greeting_msg(msg_val):
    print("Hello {}".format(msg_val))

def print_error_msg():
    print("... Wrong Choice ...")

if __name__ == "__main__":
    print(div(4,2))