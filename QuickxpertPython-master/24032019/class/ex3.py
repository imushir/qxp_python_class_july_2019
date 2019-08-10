def even_odd_count(*args):
    """
    This functio will return the
    even and odd count.

    :param *args: contains variable argument
    :type *args: tuple
    :returns: even and odd cout
    :rtype: tuple
    :author: XYZ

    """
    print("Arguments are ", args)
    even_cnt, odd_cnt = 0, 0
    for each_num in args:
        if each_num % 2 == 0:
            even_cnt = even_cnt + 1
        else:
            odd_cnt = odd_cnt + 1
    return even_cnt, odd_cnt

if __name__ == "__main__":
    #rng_val = int(input("Enter end range for numbers : "))
    #numbrs = range(0, rng_val)
    numbrs = [1, 2, 3, 4, 5, 6]
    cnt_evn, cnt_odd = even_odd_count(*numbrs)
    print("%d are even numbers and %d are odd numbers " % (cnt_evn, cnt_odd))