if __name__ == "__main__":
    try:
        file_pth = "D:\\QuickxpertPython\\31032019\\tmp_files\\"
        file_name = "%s%s" % (file_pth, "test.txt")
        file_obj = open(file_name)
        for each_line in file_obj:
            val = each_line.split(" ")
            print("Each line split values are : ", val)
            if "ip" in val:
                print("Each line ", val[-1])
    except FileNotFoundError as err:
        print("File is not present .")
    except Exception as err:
        print("Main Exception is ", err)
    finally:
        file_obj.close()