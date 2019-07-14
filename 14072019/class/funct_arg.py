# type of args is tuple and type of kwargs is dictionary.

def var_args_func(e, d, *args):
    print("Frist parameter is ", e)
    print("Second parameter is ", d)
    print("Variable arguments are " , args)

def key_word_args_func(a, b, **kwrargs):
    print("First parameter is ", a)
    print("Secomd parameter is ", b)
    print("Keywords argument is", kwrargs)
    #state_code = kwrargs.get("MH")
    #print("MH code is ", state_code)
    print("MH code is ", kwrargs["MH"])

if __name__ == "__main__":
    first_num = int(input("Enter the first num : "))
    secnd_num = int(input("Enter the secnd num : "))
    days = ["Mon", "Tues", "Wed", "Sat"]
    state_code = {"MH": 12, "GA": 14, "KA": 32}
    var_args_func(first_num, secnd_num, *days)
    key_word_args_func(first_num, secnd_num, **state_code)