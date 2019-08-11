class Animal():
    def __init__(self):
        self.animal_class = "Animal"

    def get_animal_class(self):
        return self.animal_class

    def walking(self):
        print("I am Animal class I can walk")
    
    def color(self):
        print("I am Animal class I have color")

class Lion(Animal):
    def __init__(self, name, location):
        #Animal.__init__(self)
        super(Lion, self).__init__()
        self.lion_name = name
        self.lion_locatn = location
    
    def habitat_type(self):
        print("Lion eat meat")
    
    #def walking(self):     # overriding method.
     #   print("I am Lion I walk slow")    # ignores the previous output and show overriding output.
    
    def sound(self):
        print("Lion is roaring")
    
    def get_lion_details(self):
        print("Lion name is %s" % (self.lion_name))
        print("Lion live in %s" % (self.lion_locatn))
        self.sound()

if __name__ == "__main__":
    lion_obj = Lion("AAAA", "Africa")
    print("Lion class is ", lion_obj.animal_class)
    print("Lion class is ", lion_obj.get_animal_class())
    lion_obj.walking()
    lion_obj.color()
    lion_obj.get_lion_details()
    