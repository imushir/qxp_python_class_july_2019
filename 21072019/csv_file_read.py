import csv
import os

file_location = os.path.abspath(os.path.dirname(__file__))
file_name = "test.csv"
file_path = os.path.join(file_location, file_name)
file_obj = open(file_path)
csv_read_obj = csv.reader(file_obj, delimiter="|")
num_cnt = 0
for each_line in csv_read_obj:
    print("Each line is ", each_line)
    num_cnt  = num_cnt + each_line.count("10")
print("10 appears ", num_cnt, "times")
file_obj.close()