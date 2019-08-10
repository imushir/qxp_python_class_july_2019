a = int(input("Enter 1st number..  "))
b = int(input("Enter 2nd number..  "))
if(a > b and a != b):
    if(a % 2 == 0):
        print("%d is Greater and is Even number." % a)
    else:
        print("%d is Greater and Odd number." % a)
elif(a == b):
    print("Both number are Equal number:")
else:
     if(b % 2 == 0):
        print("%d is Greater and is Even number." % b)
     else:
        print("%d is Greater and Odd number." % b)