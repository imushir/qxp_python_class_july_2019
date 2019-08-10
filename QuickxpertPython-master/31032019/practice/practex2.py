if __name__ == "__main__":
    file_path = "D:\\QuickxpertPython\\31032019\\tmp_files\\"
    file_name = "%s%s" % (file_path, "demowrite.txt")
    try:
        file_obj = open(file_name, "w")
        file_obj.writelines("Hello Chandrakanth M")
    except Exception as err:
        print("Exception is",err)
    finally:
        file_obj.close()