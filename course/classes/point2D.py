from math import sqrt
from typing import Self
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point2D(x={self.x}, y={self.y})"
    
    def distance_to_origin(self) -> float:
        return sqrt(self.x**2 + self.y**2)
    
    def distance_to_other(self, other:Self)-> float:
        pass


point_a:Point2D = Point2D(5, 5)
point_b:Point2D = Point2D(6, 10)
point_joy = Point2D(3, 5)
print(point_joy)
print(point_b.distance_to_origin()) 
print(point_b.distance_to_other(point_a)) 