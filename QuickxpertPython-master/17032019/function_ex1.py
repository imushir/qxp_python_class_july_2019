
'''
def function_name(param 1, param 2...., param N):
    """
    Description of function

    :param param 1: description
    :type param 1: data types (string, tuple, list, dictionary, set)
        \
        \
        \
        \
    :param param N: description
    :type param N: data types
    :returns: description
    :rtype: data type
    :author: Name of coder

    """
    function body

    return statements
'''

def addition(a_num, b_num):
    """
    This function will perform the addition
    of two numbers.

    :param a_num: contains the number
    :type a_num: integer
    :param b_num: contains the number
    :type b_num: integer
    :returns: additon of two numbers
    :rtype: integer

    """
    add = a_num + b_num
    return add


if __name__ == "__main__":

    num_frst = int(input("Enter first number : "))
    num_scnd = int(input("Enter second number : "))
    add_result = addition(num_frst, num_scnd)
    x_result = addition(num_frst, num_scnd)
    print("Addition %s and %s is %d " % (num_frst, num_scnd, add_result))
    print("Addition %s and %s is %d " % (num_frst, num_scnd, x_result))