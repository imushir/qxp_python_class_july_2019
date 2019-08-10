num_first = input("Enter first number : ")
num_secd = input("Enter second number : ")
num_thrd = input("Enter third number : ")
x = int(num_first)
y = int(num_secd)
z = int(num_thrd)
if(z < x > y):
    print(" %d is greater " %x)
elif(z < y > x):
    print(" %d is greater " %y)
else:
    print(" %d is greater " %z)
