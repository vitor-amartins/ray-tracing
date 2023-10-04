from src.plane import Plane
from src.point import Point
from src.shape import Shape
from src.vector import Vector


class Triangle(Shape):
    def __init__(self, p0: Point, p1: Point, p2: Point, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.normal = self._calculate_normal()
        self.containing_plane = self.get_containing_plane()

    def _calculate_normal(self) -> Vector:
        v0 = self.p1.difference(self.p0)
        v1 = self.p2.difference(self.p0)
        return v0.cross(v1).normalize()

    def get_containing_plane(self) -> Plane:
        return Plane(self.p0, self.normal, self.color)

    def intersect(self, ray_origin: Point, ray_direction: Vector) -> tuple[bool, float]:
        intersect, t = self.containing_plane.intersect(ray_origin, ray_direction)
        if not intersect:
            return False, 0

        intersection_point = ray_origin.translate(ray_direction.scale(t))

        v0 = self.p1.difference(self.p0)
        v1 = self.p2.difference(self.p0)
        intersection_vector = intersection_point.difference(self.p0)

        dot00 = v0.dot(v0)
        dot01 = v0.dot(v1)
        dot11 = v1.dot(v1)
        dotP0 = intersection_vector.dot(v0)
        dotP1 = intersection_vector.dot(v1)

        inv_den = 1 / (dot00 * dot11 - dot01 * dot01)

        alpha = (dot11 * dotP0 - dot01 * dotP1) * inv_den
        beta = (dot00 * dotP1 - dot01 * dotP0) * inv_den
        gamma = 1 - alpha - beta

        if 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1 and t > 0:
            return True, t
        return False, 0

    def get_normal(self, interception_point: Point | None = None) -> Vector:
        return self.normal
