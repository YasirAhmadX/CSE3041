#23rd August (OOP Problem Stud lis obj) Yasir Ahmad 22MIA1064

class Student:
    counter = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.counter += 1

    def details(self):
        print(f"Name: {self.name}\t Age:{self.age}")
        
n = int(input("Enter number of students: "))
l = []
for i in range(n):
    n = input("Enter name: ")
    a = int(input("Enter age: "))

    l.append(Student(n,a))

print("Student details")   
for i in l:
    i.details()
    
l.sort(key = lambda x: x.name)

print("Student details(sorted): ")
for i in l:
    i.details()

