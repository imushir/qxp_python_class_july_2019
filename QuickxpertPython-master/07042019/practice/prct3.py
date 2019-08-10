import os
import csv

if __name__ == "__main__":
    file_loc = "D:\\QuickxpertPython\\07042019\\tmp_files\\"
    file_name = "tempetrature.csv"
    temp_list = ["MH: 72C", "Nasik: 2c", "Pune: 30"]
    file_path = os.path.join(file_loc, file_name)
    file_obj = open(file_path, "w", newline="\n")
    csv_write_obj = csv.writer(file_obj, delimiter="|")
    csv_write_obj.writerows(temp_list)
    file_obj.close()