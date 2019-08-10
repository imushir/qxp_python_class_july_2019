if __name__ == "__main__":
    user_cred = {"first_name": "CH", "last_name": "MO", "age": "23", "DOB": "09_06_1995"}
    user_choice = ""
    while user_choice not in ["q", "Q"]:
        print("Choice list are [first_name, last_name, age, DOB]")
        user_choice = input("Enter required choice about user from above list: ")
        try:
            #choice_rslt = user_cred[user_choice]
            choice_rslt = user_cred.get(user_choice, "Choice not exist")
            print("Your choice is {0} and it's value is {1}." \
                               .format(user_choice, choice_rslt))
            #print("Your choice is " ,user_choice, "and it's value is ", choice_rslt)
        except KeyError as inderr:
            print("Inside KeyError is")
        except Exception as err:
            print("Error is : ", err)
        finally:
            print("Closing the program.")
