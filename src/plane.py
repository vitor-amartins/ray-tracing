from src.point import Point
from src.shape import Shape
from src.vector import Vector


class Plane(Shape):
    def __init__(self, point: Point, normal: Vector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.point = point
        self.normal = normal

    def intersect(self, ray_origin: Point, ray_direction: Vector) -> tuple[bool, float]:
        den = self.normal.dot(ray_direction)
        if abs(den) > 0.0001:
            num = self.point.difference(ray_origin).dot(self.normal)
            t = num / den
            if t > 0:
                return True, t
        return False, 0

    def __str__(self):
        return f"Plane({self.point}, {self.normal})"
