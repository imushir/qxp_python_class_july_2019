if __name__ == "__main__":
    file_path = "D:\\QuickxpertPython\\31032019\\tmp_files\\"
    file_name = "%s%s" % (file_path, "demowrite.txt")
    try:
        file_obj = open(file_name, "a")
        user_cred = "fist_name: Raju\nlast_name: Patil\nage: 20\nCompany: Cogi\n"
        file_obj.write(user_cred)
    except Exception as err:
        print("Exception Error is ", err)
    finally:
        file_obj.close()
   