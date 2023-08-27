from src.point import Point
from src.vector import Vector


class Light:
    def __init__(self, position: Point, intensity: Vector):
        self.position = position
        self.intensity = intensity
