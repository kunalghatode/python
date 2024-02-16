#An Abstract cannot be instantiated; 
# we cannot create objects for the abstract class.

from abc import ABC

class Polygon(ABC):
    __count = 0
    print(__count)
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):
        print("Has 3 sides")

class Pentagon(Polygon):
    def sides(self):
        print("Has 5 sides")

p = Pentagon()
p.sides()

t = Triangle()
t.sides()