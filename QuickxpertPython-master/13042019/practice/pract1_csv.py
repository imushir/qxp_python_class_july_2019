import os
import csv

def get_temperature_read(tempere_file):
    """
    This fuction will read the date from the .txt file.

    :param tempere_file: Contains the .txt file path
    :type tempere_file: string
    :returns: temperature data
    :rtype: list of list
    :author: CBM

    """
    try:
        temp_list = []
        file_obj = open(tempere_file)
        for each_line in file_obj:
            temp_split = [each.strip() for each in each_line.split(":")]
            temp_list.append(temp_split)
        return temp_list        
    except Exception as error:
        print("Exception is", error)

def write_temperature_data(temp_data, file_write_path):
    """
    This function will write the data into .csv file.

    :param temp_data: contains temperature data
    :type temp_data: string
    :param file_write_path: contains file path
    :type file_write_path: string
    :returns: None
    :rtype: None
    :author: CBM

    """
    try:
        file_wrte_obj = open(file_write_path, "a", newline="\n")
        csv_wrte_obj = csv.writer(file_wrte_obj, delimiter="|")
        csv_wrte_obj.writerows(temp_data)
        file_wrte_obj.close()
    except Exception as error:
        print("Exception is ", error)
    
if __name__ == "__main__":

    file_loc = "D:\\QuickxpertPython\\13042019\\tmp_files\\"
    file_name = "temperature.txt"
    file_path = os.path.join(file_loc, file_name)
    temperature_data = get_temperature_read(file_path)
    csv_name = "temperture.csv"
    csv_path = os.path.join(file_loc, csv_name)
    write_temperature_data(temperature_data, csv_path)

