class Animal():
    def __init__(self):
        self.animal_class = "Animal"

    def walking(self):
        print("I am Animal class I can walk")
    
    def color(self):
        print("I am Animal class I have color")

class Horse_Male(Animal):
    def __init__(self):
        super(Horse_Male, self).__init__()
    
    def type_of_hrse_one(self):
        print("I am Male Horse")
    
    def horse_name(self):
        print("I am Bunty")
    
    def horse_color(self):
        print("Male Horse Colour is Black")

class Horse_Female(Horse_Male):
    def __init__(self):
        super(Horse_Female, self).__init__()

    def horse_two_name(self):
        print("I am Sweety")
    
    def type_of_hrse_two(self):
        print("I am Female Horse")
    
    def horse_color_two(self):
        print("Female Hourse Colour is White")


if __name__ == "__main__":
#    male_hrse_obj = Horse_Male()
#    print("My class is ", male_hrse_obj.animal_class)
    fmle_hrse_obj = Horse_Female()
    print("My class is ", fmle_hrse_obj.animal_class)
    fmle_hrse_obj.horse_color()
    fmle_hrse_obj.horse_color_two()
    fmle_hrse_obj.color()
    fmle_hrse_obj.horse_two_name()
    fmle_hrse_obj.horse_name()