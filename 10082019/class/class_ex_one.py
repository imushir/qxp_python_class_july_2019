class Testing:
    """
    Class doc

    """
    country = "India"

    def __init__(self, msg):
        self.greet_msg = msg
        self.error_msg = "404 not found."

    def print_greet_msg(self):
        print("Message is ", self.greet_msg)
        self.print_error()
    
    def print_error(self):
        print("Error is ", self.error_msg)

if __name__ == "__main__":

    msg_val = input("Enter Greeting Message : " )
    test_obj = Testing(msg_val)
    test_obj_one = Testing("Good Hello Hi")
    test_obj.print_greet_msg()
    test_obj_one.print_greet_msg()
    print("Country is ", Testing.country)
    print("Country is ", test_obj_one.country)
    print("Country is ", test_obj.country)