import os
file_location = os.path.abspath(os.path.dirname(__file__))
days = ["MONDAY", "TUESDAY", "WEDNESDAY",
        "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY\n"]
file_name = "test_file_write.txt"
file_path = os.path.join(file_location, file_name)
#file_obj = open(file_path, "w")  # To open file in write mode
file_obj = open(file_path, "a")  # To open file in append mode
"""
file will create if not exists in write mode and old content will overwrite

"""
file_obj.write("Hello world\n")
file_obj.writelines(days) 
file_obj.close()