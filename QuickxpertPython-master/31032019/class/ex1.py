if __name__ == "__main__":
    try:
        file_pth = "D:\\QuickxpertPython\\31032019\\tmp_files\\"
        file_name = "%s%s" % (file_pth, "test.txt")
        file_obj = open(file_name)
        stream_data = file_obj.readlines()
        print("Contains of file is ", stream_data)
    except FileNotFoundError as err:
        print("File is not present .")
    except Exception as err:
        print("Main Exception is ", err)
    finally:
        file_obj.close()