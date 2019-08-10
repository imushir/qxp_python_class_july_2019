if __name__ == "__main__":
    file_path = "D:\\QuickxpertPython\\07042019\\tmp_files\\"
    file_name = "%s%s"% (file_path, "state_capital.txt")
    user_count = int(input("Please enter required number of state and capital: "))
    state_capital_list = []
    for each_list in range(user_count):
        user_state = input("Enter state name: ")
        user_capital = input("Enter capital name: ")
        state_capital_list.append("state {} and it's capital is {}\n" \
                                  .format(user_state, user_capital))
    try:
        file_obj = open(file_name, "a")         
        file_obj.writelines(state_capital_list)     
    except Exception as error:
        print("Exception is", error)
    finally:
        file_obj.close()

