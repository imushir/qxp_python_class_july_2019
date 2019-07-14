# for loop and while loop

"""
days = ["Monday", "Tuesay","Wed", "Thur", "Fri", "Sat", "Sun"]
for each_day in days:
    if each_day == "Sun":
        print("Today is", each_day, "and holiday..")
    if each_day.startswith("S"):
        print(each_day, "Its weekends")
"""
days_color = {"Mon": "Red", "Tue": "Green", "Wed": "Blue"}
for day, color in days_color.items():
    print("Day ", day)
    print("Color ", color)


for element in days_color.items():
    print("Day ", element[0])
    print("Color ", element[1])    
"""

a = 0
while(a < 10):
    a = a + 1
    if a == 5:
        break
    print("Number is ", a)
"""