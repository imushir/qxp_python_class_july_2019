import csv
file_pth = "D:\\qxp_python_class_july_2019\\21072019\\test.csv"
file_obj = open(file_pth, "a", newline="")
#csv_read_obj = csv.reader(file_obj)
csv_write_obj = csv.writer(file_obj, delimiter="|")
csv_write_obj.writerow(["HI", "Hello"])