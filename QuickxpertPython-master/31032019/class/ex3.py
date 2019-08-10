if __name__ == "__main__":
    file_pth = "D:\\QuickxpertPython\\31032019\\tmp_files\\"
    file_name = "%s%s" % (file_pth, "write_test.txt")
    file_obj = open(file_name, "w")
    #file_obj.write("Hello world")
    cntn_vals = ["Red\t", "Blue\t", "Yellow\t", "Voilet\t"]
    file_obj.writelines(cntn_vals)
    file_obj.close()
