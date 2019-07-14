def temperature_fahernt(temp_val, msg="Good Morning"):
    """
    This funtion will return the temperature in Farenhite.

    :param temp_val: contains temperature value in Celsius.
    :type temp_val: integer
    :param msg: contains welcome message.
    :type msg: string
    :returns: temperature in fahernhite and print the welcome message
    :rtype: float
    :author: QXP

    """
    far_temp = (temp_val * 9/5) + 32
    print("Message is ", msg)
    return far_temp

if __name__ == "__main__":

    tmp_val = int(input("Enter temperature Value: "))
    frn_val = temperature_fahernt(tmp_val, msg="Good Evening")
    print("Temperarur in Farenhite is ", frn_val)