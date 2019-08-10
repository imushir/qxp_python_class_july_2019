def var_argument(*args):
    print("Variable argument are  ", args)
    print("Type of argument are : ", type(args))

if __name__ == "__main__":
    a = ["red", "yellow", "mumbai", "dubai00", [1,2, 3, 4]]
    var_argument(*a)