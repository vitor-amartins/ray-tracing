from src.point import Point
from src.color import Color


class Light:
    def __init__(self, position: Point, color: Color):
        self.position = position
        self.color = color
