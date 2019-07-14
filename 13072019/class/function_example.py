def add_num(first_num, secnd_num):
    """
    This funtion will add the two numbers.

    :param first_num: contains the first number
    :type first_num: integer
    :param secnd_num: contains the second number
    :type secnd_num: integer:
    :returns: addition of two numbers.
    :rtype: integer
    :author: QXP

    """
    add_result = first_num + secnd_num
    return add_result

if __name__ == "__main__":

    x_num = int(input("Enter first num : "))
    y_num = int(input("Enter second num : "))
    result = add_num(x_num, y_num)
    print("Addition of ", x_num, "and", y_num, "is", result)