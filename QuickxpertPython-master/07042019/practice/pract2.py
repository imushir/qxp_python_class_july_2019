import os
import csv

if __name__ == "__main__":
    file_loc= "D:\\QuickxpertPython\\07042019\\tmp_files\\"
    file_name = "test.csv"
    fruits_colour_list = []
    user_count = int(input("Enter the total number of fruits and it's clours: "))
    for each_list in range(user_count):
        fruit = input("Enter the fruit name: ")
        f_colour = input("Enter the above mentioned fruit colour: ")
        fruits_colour_list.append([fruit, f_colour])
    #print(fruits_colour_list)
    file_path = os.path.join(file_loc, file_name)
    file_obj = open(file_path, "a", newline="\n")
    csv_write_obj = csv.writer(file_obj, delimiter="|")
    csv_write_obj.writerows(fruits_colour_list)
    file_obj.close()