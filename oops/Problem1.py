#23rd August (OOP Problem Area) Yasir Ahmad 22MIA1064

class Room:
    def __init__(self):
        self.a = int(input("Enter length: "))
        self.b = int(input("Enter breadth: "))

    def calc_area(self):
        return self.a*self.b

room = Room()

ar = room.calc_area()

print(f"Area of room1 is: {ar}")

room2 = Room()

print(f"Area of room2 is: {room2.calc_area()}")
