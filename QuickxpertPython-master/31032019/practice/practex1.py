if __name__ == "__main__":
    try:
        file_path = "D:\\QuickxpertPython\\31032019\\tmp_files\\"
        file_name = "%s%s" %(file_path, "demo.txt")
        file_obj = open(file_name)
        stream_line = file_obj.readlines()
        print("Given file contains :", stream_line)
        file_obj.close()
    except Exception as err:
        print(" Excepttion erroris", err)