class Klasse:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def function(self):
        print("Hi, ich heiße", self.name, "und ich bin", self.age)


p1 = Klasse("John", 36)
p1.function()
p1.age = 10
p1.name = "Lümmel"
p1.function()
#   del p1.age (Löscht age in p1(property))
#   del p1 (Löscht Objekt P1)

#   class definitions cannot be empty
#   but if you for some reason have a class definition with no content
#   put in the pass statement to avoid getting an error.
