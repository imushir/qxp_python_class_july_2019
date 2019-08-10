if __name__ == "__main__":
    file_pth = "D:\\QuickxpertPython\\31032019\\tmp_files\\"
    file_name = "write_test.txt"
    actual_file = "%s%s" % (file_pth, file_name)
    try:
        file_obj = open(actual_file, "a")
        file_obj.write("%s%s" % ("Demoo", "\n"))
    except Exception as err:
        print("Error is ", err)
    finally:
        file_obj.close()