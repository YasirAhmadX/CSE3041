#23rd August (OOP Stud class) Yasir Ahmad 22MIA1064

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details(self):
        print(self.name)
        print(self.age)

a = Student("YSR",39)
b = Student("AMD",26)

print("type of a:",type(a))

a.details()
b.details()

print(f"{a.name} is of age {a.age} yr")
