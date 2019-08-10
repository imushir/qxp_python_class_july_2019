fruits = {"Apple": "Red", "Grape": "Green", "Mango": "Yellow"}
num_square = {}
for each_val in fruits.items():
    key, val = each_val
    print("%s color is %s " % (key, val))
for num in range(1, 11):
    num_square.update({num: num ** 2})
print("Square numbers : ", num_square)