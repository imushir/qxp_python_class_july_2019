

a = 5    # Integer
b = 3.14 # Float
note = "Welcome to Python.." # String
tup_val = ("Red", "Blue", "Pink")
list_val = [1, 2, 3, "Demo", "Tea", "Coffee"]
print(len(note))  # to find the number of element
a_val = list_val[0]
print("Length of list is ", len(list_val))
print("List val is ", a_val)
print("Values using slicing are : ", list_val[: 4])
print("Color values are : ", tup_val[1])
print("Methods of list are : ", dir(list_val)) # to check attribute and methodsof object
list_val.append("Thane")
print("New list is ", list_val)
list_val.extend([100, 200, 300])
print("New values after extend is ", list_val)


alpha_map = {1: "A", 2: "B", 3: "C"}
print("Firts alphabet is : ", alpha_map.get(4, "Not Valid"))