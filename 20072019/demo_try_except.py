a_num = 8
a_val = [1, 2, 0, 4, 8, 6, 7]
for each_num in a_val:
    try:
        result = a_num / each_num
        print("Division is :", result)
    except ZeroDivisionError as err:
        print("Caanot divide by Zero", err)
    except IndexError as index_err:
        print("List is too small", index_err)
    except Exception as base_err:
        print("Error is ", base_err)
    else:
        print("Completed Division")
    finally:
        print("Clean Activity")
