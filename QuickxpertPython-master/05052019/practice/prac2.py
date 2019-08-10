import os

class FileHandling(object):
    def __init__(self, filename):
        self.file_name = filename

    def get_file_content(self):
        match_details = {}
        read_file_obj = open(self.file_name)
        for each_line in read_file_obj:
            if each_line:
                #print("Each line ", each_line)
                line_field = each_line.split(":")
                #print("Data after split", line_field)
                match_name = line_field[0].strip()
                #print("Match name is ", match_name)
                match_score = line_field[1].strip()
                #print("Match score is ", match_score)
                match_details[match_name] = match_score
        read_file_obj.close()
        return match_details

    def put_in_file(self, match_score_line):
        write_file_obj = open(self.file_name, "a")
        write_file_obj.write("%s\n" % (match_score_line))
        write_file_obj.close()

if __name__ ==  "__main__":

    file_pth = "D:\\QuickxpertPython\\05052019\\tmp_files\\"
    file_name = "match_score.txt"
    match_nm_val = input("Enter match name : ")
    match_score = input("Enter match score : ")
    actual_file = os.path.join(file_pth, file_name)
    file_class_obj = FileHandling(actual_file)
    if match_score.isdigit():
        match_score_val = int(match_score)
        match_data = "%s : %d" % (match_nm_val, match_score_val)
        file_class_obj.put_in_file(match_data)  
    else:
        print("Enter only Numeric values.")
    match_info = file_class_obj.get_file_content()
    print("Match info is ", match_info)

