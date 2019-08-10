import os
import csv


if __name__ == "__main__":
    file_loc = "D:\\QuickxpertPython\\07042019\\tmp_files\\"
    file_name = "test.csv"
    file_pth = os.path.join(file_loc, file_name)
    try:
        file_obj = open(file_pth)
        csv_read_obj = csv.reader(file_obj)
        for index, each_row in enumerate(csv_read_obj):
            if index == 0:
                continue
            first_name = each_row[0]
            last_name = each_row[1]
            designation = each_row[4]
            salary_val = each_row[5]
            print("Firtname is {}, lastname is {}, designation is {}," \
                  "salary is {}".format(first_name, last_name, \
                  designation, salary_val))
        csv_read_obj.close()
    except Exception as error:
        print("File Does not exists")