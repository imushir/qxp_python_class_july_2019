import os
#file_location = "D:\\qxp_python_class_july_2019\\20072019\\test_file.txt"
file_location = os.path.abspath(os.path.dirname(__file__))
file_name = "test_file.txt"
file_path = os.path.join(file_location, file_name)
if os.path.isfile(file_path) and file_name.endswith(".txt"):
    file_obj = open(file_path)
    file_content = file_obj.readlines()
    print("File content is ", file_content)
    for each_line in file_content:
        print("Each line ", each_line.strip())
    """
    for each_line in file_obj:
        print("Each line is ", each_line.strip())
    """
else:
    print("Invalid file extension")