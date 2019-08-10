import os
import csv

if __name__ == "__main__":
    file_loc = "D:\\QuickxpertPython\\07042019\\tmp_files"
    file_name = "test.csv"
    user_dta = []
    labels_fields = ["Firstname", "Lastname", "DOB", "DOJ",
                  "Department", "Salary"]
    for each_label in labels_fields:
        user_val = input("Enter {}: ".format(each_label))
        user_dta.append(user_val)
    file_pth = os.path.join(file_loc, file_name)
    file_obj = open(file_pth, "a", newline="\n")
    csv_write_obj = csv.writer(file_obj, delimiter="$")
    csv_write_obj.writerow(user_dta)
    #csv_write_obj.writerow(["DDDD", "EEEE", "09/08/1992", "07/06/2017", \    # to take single row
    #                     "IT", "50000"])
    #csv_write_obj.writerows([["AAAA", "BBBB", "09/09/1990", "06/07/2013",    # to take more than one row
    #                         "Acc", "1000"], ["XXXX", "YYYY", "07/10/1990",
    #                         "03/07/2015", "Mech", "1000"]])
    file_obj.close()