def default_param(temp_val, convrt_rate=32):
    """
    This function will return the Farenhite temperature
    or Celsius temperature value

    :param temp_val: contains temperature value
    :type temp_val: integer
    :param convrt_rate: contains converter rate
    :type convrt_rate: integer
    :returns: converted temperature
    :rtype: integer
    :author: XYZ

    """
    cnvrt_temp = temp_val + convrt_rate
    return cnvrt_temp


if __name__ == "__main__":
    temperature_val = 0
    rate_type = ""
    while rate_type != "q":
        rate_type = input("Enter the Rate type F or f or k or K : ")
        temperature_val = int(input("Enter the temperature : "))
        if rate_type == "F" or rate_type == "f":
        #if rate_type in ["F", "f"]:
            result_temp = default_param(temperature_val)
        elif rate_type == "k" or rate_type == "K":
        #elif rate_type in ["K", "k"]:
            result_temp = default_param(temperature_val, convrt_rate=273)
        else: 
            break
        print("Coverted tempature is %d " % result_temp)
