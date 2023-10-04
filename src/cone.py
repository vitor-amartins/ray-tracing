import math

from src.point import Point
from src.shape import Shape
from src.vector import Vector


class Cone(Shape):
    def __init__(self, apex: Point, axis_direction: Vector, angle: float, height: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apex = apex
        self.axis_direction = axis_direction.normalize()
        self.angle = math.radians(angle)
        self.height = height

    def intersect(self, ray_origin: Point, ray_direction: Vector):
        oc = ray_origin.difference(self.apex)

        # Define a altura máxima do cone
        h = self.height

        a = ray_direction.dot(ray_direction) - (1 + math.tan(self.angle) ** 2) * ray_direction.dot(
            self.axis_direction) ** 2
        b = 2 * (ray_direction.dot(oc) - (1 + math.tan(self.angle) ** 2) * ray_direction.dot(
            self.axis_direction) * oc.dot(self.axis_direction))
        c = oc.dot(oc) - (1 + math.tan(self.angle) ** 2) * oc.dot(self.axis_direction) ** 2

        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            t1 = (-b - math.sqrt(discriminant)) / (2 * a)
            t2 = (-b + math.sqrt(discriminant)) / (2 * a)
            if t1 > 0 and 0 <= oc.add(ray_direction.scale(t1)).y <= h:
                return True, t1
            if t2 > 0 and 0 <= oc.add(ray_direction.scale(t2)).y <= h:
                return True, t2
        return False, None

    def get_normal(self, intersection_point: Point) -> Vector:
        # Calcula a normal no ponto de interseção
        dis = intersection_point.distanceTo(self.apex)
        D = dis * math.sqrt(1 + math.tan(self.angle) ** 2)
        A = self.apex.translate(self.axis_direction.scale(D))
        return intersection_point.difference(A).normalize()
