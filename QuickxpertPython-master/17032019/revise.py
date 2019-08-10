"""
firstNum = input("Enter first Number : ")
secndNum = input("Enter Second Number : ")
x_num = int(firstNum)
y_num = int(secndNum)
if(y_num % 2 == 0):
    print("%d is even number." % (y_num))
    if(y_num > x_num):
        print("%d is greater than %d." % (y_num, x_num))
    else:
        print("%d is greater than %d ." % (x_num, y_num))
else:
    print("%d is even number." % (x_num))
    if(x_num > y_num):
        print("%d is greater than %d." % (x_num, y_num))
    else:
        print("%d is greater than %d." % (y_num, x_num))
"""
"""
range_value = input("Enter the end range value : ")
nums = range(int(range_value))
evn_cnt = 0
odd_cnt = 0
multiple_fvn_cnt = 0
for each_num in nums:
    if each_num % 2 == 0:
        evn_cnt = evn_cnt + 1
    elif each_num % 5 == 0:
        multiple_fvn_cnt = multiple_fvn_cnt + 1
    else:
        odd_cnt = odd_cnt + 1
print("Number of even numbers are : ", evn_cnt)
print("Number of odd numbers are : ", odd_cnt)
print("Multiple of five numbers are : ", multiple_fvn_cnt)
"""

"""
tmp = [1, 2, 3, 4, "N", 5, 6, 8]
tmp_len = len(tmp)
index = 0
while True:
    val = tmp[index]
    print("Value is ", val)
    index = index + 1
    if val == "N":
        continue
    elif index == tmp_len:
        break
"""





