import math

from src.vector import Vector


class Point:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def distanceTo(self, other: 'Point') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    def difference(self, other: 'Point') -> Vector:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def translate(self, vector: Vector) -> 'Point':
        return Point(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
