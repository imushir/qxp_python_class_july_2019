class Animal:
    def __init__(self, animal_name, animal_color):
        self.__animl_name = animal_name
        self.__animl_color = animal_color
    
    def get_animal_details(self):
        return "Name : {} Color {}".format(self.__animl_name, self.__animl_color)

if __name__ == "__main__":

    ani_one_obj = Animal("Cat", "White")
    details = ani_one_obj.get_animal_details()
    print(details)