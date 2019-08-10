# Indexerror exception

if __name__ == "__main__":
    user_choice = "y"
    while user_choice == "y":
        fruit_names = ["apple", "mango", "grapes", "pineapple",
                    "banana", "jackfruit", "watermelon"]
        fruit_len = len(fruit_names)
        print("Fruits list is : ", fruit_names)
        try:
            for each_index in range(0, fruit_len + 1):
                fruit_nm = fruit_names[each_index]
        except IndexError as indx_err:
            print("Got error ", indx_err)
        except Exception as err:
            print("Base Exception is ", err)
        finally:
            nw_fruit = input("Enter new fruit name : ")
            nw_frt_nm = nw_fruit.lower()
            if nw_frt_nm not in fruit_names:
                fruit_names.append(nw_frt_nm)
                print("{} added in fruits list.".format(nw_frt_nm))
                print("New fruit list is ", fruit_names)
            else:
                print("{} already in fruits list".format(nw_frt_nm))
            user_choice = input("Do you want to continue y/Y for Yes or n/N for No ")
