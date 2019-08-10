months = ("jan", "feb", "mar", "apr", "may")
for index in range(0, len(months)):
    print("Index is ", index)
    mnt_val = months[index]
    print("Month value is ", mnt_val)
    if(mnt_val == "feb"):
        print("%s Month is %d" % (mnt_val, index + 1))
    else:
        print("Months")