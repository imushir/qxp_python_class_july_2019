month_maps = {}
months = ["Jan", "Feb", "Mar", "April", "May",
          "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

for each_index in range(0, len(months)):
    month_maps[each_index + 1] = months[each_index]

print("Months dictionary is ", month_maps)

