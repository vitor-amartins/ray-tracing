import math

from src.point import Point
from src.shape import Shape
from src.vector import Vector


class Sphere(Shape):
    def __init__(self, center: Point, radius: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius

    def intersect(self, ray_origin: Point, ray_direction: Vector) -> tuple[bool, float]:
        ray_to_center: Vector = self.center.difference(ray_origin)

        a = ray_direction.dot(ray_direction)
        b = -2 * ray_to_center.dot(ray_direction)
        c = ray_to_center.dot(ray_to_center) - self.radius * self.radius

        discriminant = b * b - 4 * a * c

        if discriminant > 0:
            discriminant_sqrt = math.sqrt(discriminant)
            t1 = (-b - discriminant_sqrt) / (2 * a)
            t2 = (-b + discriminant_sqrt) / (2 * a)
            if t1 > 0 or t2 > 0:
                return True, min(t1, t2)
        return False, 0
