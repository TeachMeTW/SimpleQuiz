class Student: # defines datatype

    def __init__(self, name, major, gpa, sex, age): # map attributes of datatype | an object
        self.name = name # stores these values
        self.major = major # ex: major entry = student's major
        self. gpa = gpa
        self.sex = sex
        self.age = age
    def has_honors(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

class Chef:

    def make_BEEF(self):
        print("Yo i got sum beef w/ u")

    def make_salad(self):
        print("Here ya go u vegan")

    def make_special(self):
        print("OwO sempai its got special ingredients")