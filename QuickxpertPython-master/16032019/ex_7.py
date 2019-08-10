code = input("Enter State code..  ")
states = [("Maharashtra", "MH"), ("KARNATKA", "KA"), ("DELHI", "DH")]
for each_state in states:
    state_val, state_cd = each_state
    if code == state_cd:
        if state_cd == "MH":
            print("Temprature for %s is 10 celsius." % (state_val))
        elif state_cd == "KA":
            print("Temprature for %s is 35 celsius." % (state_val))
        elif state_cd == "DH":
            print("Temperature for %s is  45 celsius." % (state_val))
    else:
       continue