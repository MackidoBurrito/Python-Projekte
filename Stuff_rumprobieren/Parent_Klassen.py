class Teacher:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Teacher("Max", "Mustermann")
x.printname()


class Student(Teacher):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Moin", self.firstname, self.lastname, "nicht verzweifeln, denn", self.graduationyear, "wirst du fertig sein!")


x = Student("Monika", "Mustermann", 2077)
x.welcome()
