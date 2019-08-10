def key_word_argument(a, *args, **kwrgs):
    print("Required variable is : ", a)
    print("Variable args is : ", args)
    print("Key word argument ", kwrgs)
    print("Type of Key wordargument ", type(kwrgs))


if __name__ == "__main__":
    usr_cred = {"first_name": "AAA", "last_name": "BBB", "gender": "M", \
                 "DOB": "11/12/1990"}
    key_word_argument(*usr_cred, **usr_cred)
    #key_word_argument(1, x="a", b="b", c="c")
    #key_word_argument(**usr_cred)